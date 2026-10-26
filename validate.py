#!/usr/bin/env python3
"""Validate every packs/products/*/pack.yaml against pack.schema.json plus cross-reference checks."""
import json, sys, glob, os, yaml
from jsonschema import Draft202012Validator
schema = json.load(open(os.path.join(os.path.dirname(__file__), 'schema', 'pack.schema.json')))
paths = sys.argv[1:] or glob.glob('packs/products/*/pack.yaml')
bad = 0
for p in paths:
    d = yaml.safe_load(open(p, encoding='utf-8'))
    errs = [f"{'/'.join(map(str, e.path)) or '<root>'}: {e.message}" for e in Draft202012Validator(schema).iter_errors(d)]
    if not errs:
        cards = {c['id'] for c in d['fix_cards']}; syms = {s['id'] for s in d['symptoms']}
        for s in d['symptoms']:
            if s['fix_card'] not in cards: errs.append(f"symptom {s['id']} points to unknown fix card {s['fix_card']}")
        for c in d['fix_cards']:
            if c['if_not_fixed'] == 'try_next_card' and c.get('next_card') not in cards: errs.append(f"fix card {c['id']} needs a valid next_card")
            for i, st in enumerate(c['steps']):
                if st['safety_stop'] and not st.get('stop_if'): errs.append(f"fix card {c['id']} step {i+1}: safety_stop needs stop_if")
        for e in d.get('error_codes', []):
            if e['symptom'] not in syms: errs.append(f"error code {e['code']} points to unknown symptom {e['symptom']}")
        for g in d['golden_cases']:
            if g['expect_symptom'] not in syms: errs.append(f"golden {g['id']}: unknown symptom {g['expect_symptom']}")
            if g['expect_fix_card'] not in cards: errs.append(f"golden {g['id']}: unknown fix card {g['expect_fix_card']}")
            if g['expect_outcome'] == 'safety_stop' and not g.get('expect_safety_stop'): errs.append(f"golden {g['id']}: safety_stop outcome needs expect_safety_stop: true")
        ids = [g['id'] for g in d['golden_cases']]
        if len(ids) != len(set(ids)): errs.append('duplicate golden case ids')
        if not any(s['safety_stop'] for c in d['fix_cards'] for s in c['steps']): errs.append('pack has no safety stop anywhere — every pack needs at least one')
    print(('OK   ' if not errs else 'FAIL ') + p)
    for e in errs: print('   -', e)
    bad += bool(errs)
sys.exit(1 if bad else 0)
