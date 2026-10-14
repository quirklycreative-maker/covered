# Covered India claim templates, 0.3.0 (draft)

> Generated from `templates.yaml` and `country.yaml`. Do not edit by hand.
> This is information, not legal advice. Covered drafts the paper; the user decides whether to send or file it.
> Hindi review: **pending**. Every Hindi line needs a native reader before release.

## e-Jagriti upload set

| Upload | Template | Note |
|---|---|---|
| Index | `index` |  |
| Proforma | `district_commission_complaint` | Read as the complaint set out in the NCDRC proforma order. Unconfirmed; the manual does not define it. |
| Synopsis | `synopsis_list_of_dates` |  |
| Memo of Parties | `memo_of_parties` |  |
| Notarized Affidavit | `affidavit` |  |
| Vakalatnama | none | Only when the user chooses to file through an advocate (routes.filing_mode). The advocate supplies it; Covered gives no template. A self-filing user skips it. |
| Annexures | none | Your own files: bill, warranty card, photos, service records, letters. Label them Annexure A-1, A-2 and so on. |

## 1. Written complaint to the brand and the seller
*ब्रांड और विक्रेता को लिखित शिकायत*

`brand_seller_letter`

**Note:** Always the first step. reply_days is your own deadline, not a legal period. Two remedy lines exist: use the in-warranty one only if the product is in warranty. If it is out of warranty, use the second one, which does not claim a free repair.

**Note (hi):** यही हमेशा पहला कदम है। reply_days आपकी अपनी समय-सीमा है, कानूनी अवधि नहीं। उत्पाद वारंटी में हो तभी पहली पंक्ति चुनें। वारंटी खत्म हो चुकी हो तो दूसरी पंक्ति लें, जिसमें मुफ़्त मरम्मत का दावा नहीं है।

**Legal basis (rule, verification, source):**

- `brand_first` (product_decision): Product rule: the user always contacts the brand or seller first. The NCH form itself asks whether the grievance was registered with the company. Source: [Team decision recorded in the Country Pack India review answers, 10 Oc](https://github.com/), [NCH Grievance Registration Form, screenshots captured by the team afte](https://consumerhelpline.gov.in/user/register-complaint.php)
- `defect_definition` (secondary_only): Defect: any fault, imperfection or shortcoming in quality, quantity, potency, purity or standard required by law, by contract (express or implied) or as claimed by the trader. CPA 2019 s.2(10). A breakdown alone does not prove a statutory defect. Source: [CPA 2019 s.2 Definitions (AdvocateKhoj)](https://www.advocatekhoj.com/library/bareacts/consumerprotection2019/2.php?Title=Consumer+Protection+Act%2C+2019&STitle=Definitions), [CPA 2019 s.2 Definitions (consumerprotection.in), clause cross-check](https://www.consumerprotection.in/section-2-definitions/), [Consumer Protection Act, 2019 - PRS India reproduction (text ends befo](https://PRSINDIA.org/files/bills_acts/bills_parliament/2021/Consumer%20Protection%20Act%202019.pdf), [Consumer Protection Act, 2019 - India Code record (text not opened by ](https://www.indiacode.nic.in/handle/123456789/15256)
- `nch_is_prelitigation` (primary_checked): The National Consumer Helpline is a free pre-litigation route. It forwards the grievance to the company and may take up to 30 days. More than 2,000 companies take part in the Convergence programme. Source: [National Consumer Helpline - About](https://consumerhelpline.gov.in/public/about), [National Consumer Helpline - Convergence programme](https://consumerhelpline.gov.in/public/convergenceprogram)
- `warranty_source_order` (product_decision): Product rule: (1) the user's warranty card or invoice; (2) if none, the app helps the user find the terms on the brand site or the Right to Repair portal; (3) only if the user cannot find them, the product pack's typical value, marked assumed, with a visible notice. The user's own card always overrides the pack. Source: [Team decision recorded in the Country Pack India review answers, 10 Oc](https://github.com/), [Right to Repair portal launch and contents (Business Standard)](https://www.business-standard.com/technology/tech-news/right-to-repair-how-to-access-it-what-it-covers-and-consumer-benefits-123052200523_1.html), [Godrej AC extended PCB warranty scheme, Gujarat, May-June 2021 (one br](https://godrejenterprises.com/Resources/Support/ACExtendedPCBwarrantyJune21Gujarat_21045647.pdf)
- `warranty_start_not_fixed_by_law` (primary_checked): The CCPA asked brands in June 2024 to disclose before sale whether the warranty starts at purchase or installation. It did not make installation the rule. The start point stays brand-specific. Source: [PIB, 22 Jun 2024: CCPA meeting on warranty start date (purchase vs ins](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2027925)
- `proof_of_defect_evidence` (secondary_only): Case reports: the complainant must prove a manufacturing defect, and an NCDRC order required expert opinion for an inherent defect in a vehicle; repeated breakdowns and a record of failed repair attempts carried weight in other orders. Not law; shapes the evidence advice. Source: [News reports of NCDRC and District Commission orders on proof of defec](https://www.livelaw.in/consumer-cases/ncdrc-burden-of-proof-manufacturing-defect-complainant-260956)

**Slots** (the app drops empty slots and picks the option that fits):

- `{imei_line}`: Phones only, when the IMEI is known. Drop the line otherwise.
  - `present`: IMEI: {imei}.
    - हिन्दी: IMEI: {imei}।
- `{installation_line}`: Products installed by the brand or a technician (AC, TV, refrigerator). Drop the line otherwise.
  - `present`: Installation date: {installation_date}.
    - हिन्दी: इंस्टॉलेशन की तारीख: {installation_date}।
- `{registration_line}`: When a product registration number exists. Drop the line otherwise.
  - `present`: Product registration number: {product_registration_no}.
    - हिन्दी: उत्पाद पंजीकरण संख्या: {product_registration_no}।
- `{warranty_line}`: Pick by the coverage result.
  - `in_warranty`: Warranty: up to {warranty_until}, counted from {warranty_start_text}, as stated in {warranty_source_text}.
    - हिन्दी: वारंटी: {warranty_until} तक, {warranty_start_text} से गिनी हुई, जैसा {warranty_source_text} में लिखा है।
  - `assumed`: Warranty: I understand it runs up to {warranty_until}. This is the usual period for this kind of product; I could not find the brand's own terms. Please confirm the exact terms in writing.
    - हिन्दी: वारंटी: मेरी जानकारी में यह {warranty_until} तक है। यह इस तरह के उत्पाद की आम अवधि है; मुझे कंपनी की अपनी शर्तें नहीं मिलीं। कृपया सही शर्तें लिखित में बताएँ।
  - `ended`: The warranty ended on {warranty_until}. The fault first appeared on {fault_first_seen}.
    - हिन्दी: वारंटी {warranty_until} को खत्म हुई। खराबी पहली बार {fault_first_seen} को आई थी।
- `{defect_origin_line}`: Only when the user believes the fault comes from how the product was made. Never write it for damage the user caused.
  - `manufacturing`: I believe this is a manufacturing defect because {defect_reason}.
    - हिन्दी: मेरा मानना है कि यह निर्माण-दोष (manufacturing defect) है, क्योंकि {defect_reason}।
- `{technician_report_line}`: Team proposal, not yet agreed. Only when an authorised service centre has written a finding.
  - `present`: An authorised service centre has recorded in writing that {technician_finding} (copy attached).
    - हिन्दी: अधिकृत सर्विस सेंटर ने लिखित में दर्ज किया है कि {technician_finding} (प्रति संलग्न)।
- `{remedy_line}`: Pick by the coverage result.
  - `in_warranty`: Since the product is within its warranty, I request you to {remedy_requested} at no cost to me.
    - हिन्दी: उत्पाद वारंटी अवधि में है, इसलिए अनुरोध है कि बिना किसी शुल्क के {remedy_requested}।
  - `ended_defect`: I request you to {remedy_requested}. I believe the fault is a defect in the product and not the result of use or misuse. Please inspect it and state in writing whether you accept this. If any charge is claimed, please give the reason in writing.
    - हिन्दी: अनुरोध है कि {remedy_requested}। मेरा मानना है कि खराबी उत्पाद के दोष (defect) के कारण है, उपयोग या दुरुपयोग के कारण नहीं। कृपया जाँच करके लिखित में बताएँ कि आप इससे सहमत हैं या नहीं। कोई शुल्क माँगा जाए तो उसका कारण भी लिखित में दें।

### English

```text
Date: {date}

To:
1. Customer Care, {brand}
2. {seller_name}

Subject: Complaint about defective {product}, model {model}, serial {serial}, invoice {invoice_no}

Dear Sir or Madam,

I bought a {brand} {product}, model {model}, serial number {serial}, from {seller_name} on {purchase_date} for Rs {price_inr} (invoice {invoice_no}, copy attached).
{imei_line}
{installation_line}
{registration_line}
{warranty_line}

The defect: {defect_statement}. It first appeared on {fault_first_seen}. {defect_origin_line} {technician_report_line}

What I have done so far: basic checks: {steps_tried}. Service requests: {service_requests}. Latest service request number: {service_request_no}.

What is still unresolved: {gap_statement}

{remedy_line} Please reply in writing within {reply_days} days with the date of the visit or the action you will take.

If the matter is not resolved, I will register a grievance with the National Consumer Helpline and may file a complaint before the Consumer Disputes Redressal Commission under the Consumer Protection Act, 2019.

Attached: invoice, warranty card, photographs of the defect, earlier complaint numbers{extra_attachments}.

Yours faithfully,
{user_name}
{user_address}
Phone: {user_phone}  Email: {user_email}
```

### हिन्दी

```text
दिनांक: {date}

सेवा में,
1. कस्टमर केयर, {brand}
2. {seller_name}

विषय: खराब {product} की शिकायत - मॉडल {model}, सीरियल {serial}, बिल नंबर {invoice_no}

महोदय/महोदया,

मैंने {seller_name} से {purchase_date} को {brand} कंपनी का {product}, मॉडल {model}, सीरियल नंबर {serial}, {price_inr} रुपये में खरीदा था (बिल नंबर {invoice_no}, प्रति संलग्न)।
{imei_line}
{installation_line}
{registration_line}
{warranty_line}

खराबी: {defect_statement}। यह पहली बार {fault_first_seen} को आई। {defect_origin_line} {technician_report_line}

अब तक मैंने यह किया है: बुनियादी जाँचें: {steps_tried}। सर्विस शिकायतें: {service_requests}। सबसे ताज़ा सर्विस शिकायत नंबर: {service_request_no}।

जो बात अब भी हल नहीं हुई: {gap_statement}

{remedy_line} कृपया {reply_days} दिनों के भीतर लिखित उत्तर दें, जिसमें आने की तारीख या की जाने वाली कार्रवाई बताई गई हो।

मामला हल न होने पर राष्ट्रीय उपभोक्ता हेल्पलाइन (National Consumer Helpline) में शिकायत दर्ज कराई जाएगी, और उपभोक्ता संरक्षण अधिनियम, 2019 के तहत उपभोक्ता विवाद निवारण आयोग (Consumer Disputes Redressal Commission) में शिकायत भी की जा सकती है।

संलग्न: बिल, वारंटी कार्ड, खराबी की फ़ोटो, पहले के शिकायत नंबर{extra_attachments}।

भवदीय,
{user_name}
{user_address}
फ़ोन: {user_phone}  ईमेल: {user_email}
```

## 2. Claim to the extended-warranty, AMC, insurance or card-benefit provider
*एक्सटेंडेड वारंटी, AMC, बीमा या कार्ड-लाभ देने वाले को दावा*

`plan_provider_claim`

**Note:** Claim rules come from the plan or card document, not from the law. Keep the terms at hand. Use the card variant only if the product was bought on that card and the benefit is active; purchase protection that covers only theft or accidental damage is not an extended warranty.

**Note (hi):** दावे के नियम प्लान या कार्ड के दस्तावेज़ से तय होते हैं, कानून से नहीं। शर्तें पास रखें। कार्ड वाला रूप तभी लें जब उत्पाद उसी कार्ड से खरीदा गया हो और लाभ चालू हो; जो सुरक्षा केवल चोरी या आकस्मिक नुकसान को कवर करती है, वह एक्सटेंडेड वारंटी नहीं है।

**Legal basis (rule, verification, source):**

- `card_benefit_counts` (product_decision): Product rule: a credit-card or bank extended warranty counts as a protection plan only if the user confirms the product was bought on that card and the benefit is active. Purchase protection (theft and accidental damage, short window) does not extend a warranty. No Indian statistics on card extended warranties were found. Source: [Team decision recorded in the Country Pack India review answers, 10 Oc](https://github.com/), [American Express India: extended warranty and purchase protection expl](https://www.americanexpress.com/in/articles/life-with-amex/benefits/purchase-protection.html), [ICICI Bank blog: card benefits include extended warranty (vendor page)](https://www.icici.bank.in/personal-banking/blogs/card/credit-card/hidden-benefits-of-having-credit-card), [Samsung Knox Care+ India claim steps (one plan: IMEI, alternate contac](https://docs.samsungknox.com/admin/care-plus/submit-a-claim/india/)
- `warranty_source_order` (product_decision): Product rule: (1) the user's warranty card or invoice; (2) if none, the app helps the user find the terms on the brand site or the Right to Repair portal; (3) only if the user cannot find them, the product pack's typical value, marked assumed, with a visible notice. The user's own card always overrides the pack. Source: [Team decision recorded in the Country Pack India review answers, 10 Oc](https://github.com/), [Right to Repair portal launch and contents (Business Standard)](https://www.business-standard.com/technology/tech-news/right-to-repair-how-to-access-it-what-it-covers-and-consumer-benefits-123052200523_1.html), [Godrej AC extended PCB warranty scheme, Gujarat, May-June 2021 (one br](https://godrejenterprises.com/Resources/Support/ACExtendedPCBwarrantyJune21Gujarat_21045647.pdf)
- `defect_definition` (secondary_only): Defect: any fault, imperfection or shortcoming in quality, quantity, potency, purity or standard required by law, by contract (express or implied) or as claimed by the trader. CPA 2019 s.2(10). A breakdown alone does not prove a statutory defect. Source: [CPA 2019 s.2 Definitions (AdvocateKhoj)](https://www.advocatekhoj.com/library/bareacts/consumerprotection2019/2.php?Title=Consumer+Protection+Act%2C+2019&STitle=Definitions), [CPA 2019 s.2 Definitions (consumerprotection.in), clause cross-check](https://www.consumerprotection.in/section-2-definitions/), [Consumer Protection Act, 2019 - PRS India reproduction (text ends befo](https://PRSINDIA.org/files/bills_acts/bills_parliament/2021/Consumer%20Protection%20Act%202019.pdf), [Consumer Protection Act, 2019 - India Code record (text not opened by ](https://www.indiacode.nic.in/handle/123456789/15256)

**Slots** (the app drops empty slots and picks the option that fits):

- `{subject_ref}`: Pick by the type of cover.
  - `plan`: Claim under plan number {plan_number}
    - हिन्दी: प्लान नंबर {plan_number} के तहत दावा
  - `card`: Claim under the {card_benefit_name} benefit of the {card_name} card
    - हिन्दी: {card_name} कार्ड के {card_benefit_name} लाभ के तहत दावा
- `{cover_line}`: Pick by the type of cover.
  - `plan`: is covered by your plan number {plan_number}, valid until {plan_valid_until}.
    - हिन्दी: आपके प्लान नंबर {plan_number} में कवर है, जो {plan_valid_until} तक मान्य है।
  - `card`: was bought using your {card_name} card, which carries the benefit "{card_benefit_name}". The benefit was active on the purchase date and is active now.
    - हिन्दी: आपके {card_name} कार्ड से खरीदा गया था, जिसमें "{card_benefit_name}" लाभ है। यह लाभ खरीद की तारीख पर चालू था और अब भी चालू है।

### English

```text
Date: {date}

To: {plan_provider}

Subject: {subject_ref} - {brand} {product}, model {model}, serial {serial}

Dear Sir or Madam,

My {brand} {product}, model {model}, serial number {serial}, bought on {purchase_date} (invoice {invoice_no}), {cover_line}

Since {fault_first_seen}, it has this fault: {defect_statement}. I tried these basic checks: {steps_tried}. The fault remains.

I request you to {remedy_requested} under the cover, and to reply in writing within {reply_days} days with the claim number and the next steps.

Attached: plan or card benefit document, invoice, photographs of the defect.

Yours faithfully,
{user_name}
{user_address}
Phone: {user_phone}  Email: {user_email}
```

### हिन्दी

```text
दिनांक: {date}

सेवा में: {plan_provider}

विषय: {subject_ref} - {brand} कंपनी का {product}, मॉडल {model}, सीरियल {serial}

महोदय/महोदया,

{purchase_date} को खरीदा गया मेरा {brand} कंपनी का {product}, मॉडल {model}, सीरियल नंबर {serial} (बिल नंबर {invoice_no}), {cover_line}

{fault_first_seen} से इसमें यह खराबी है: {defect_statement}। मैंने ये बुनियादी जाँचें कीं: {steps_tried}। खराबी अब भी है।

अनुरोध है कि इस कवर के तहत {remedy_requested}, और {reply_days} दिनों के भीतर लिखित में दावा नंबर और आगे की प्रक्रिया बताएँ।

संलग्न: प्लान या कार्ड-लाभ का दस्तावेज़, बिल, खराबी की फ़ोटो।

भवदीय,
{user_name}
{user_address}
फ़ोन: {user_phone}  ईमेल: {user_email}
```

## 3. Grievance for the National Consumer Helpline
*राष्ट्रीय उपभोक्ता हेल्पलाइन के लिए शिकायत*

`nch_grievance`

**Note:** The text goes into the form field 'Grievance details'. The other form fields are in form_map. The form was read from screenshots after login; the drop-down values were not captured, so the app shows a hint and the user picks from the list.

**Note (hi):** यह पाठ फ़ॉर्म के 'Grievance details' खाने में जाता है। फ़ॉर्म के बाकी खाने form_map में हैं। फ़ॉर्म लॉगिन के बाद के स्क्रीनशॉट से पढ़ा गया; ड्रॉप-डाउन के विकल्प नहीं मिले, इसलिए ऐप संकेत दिखाता है और उपयोगकर्ता सूची से चुनता है।

**Legal basis (rule, verification, source):**

- `nch_is_prelitigation` (primary_checked): The National Consumer Helpline is a free pre-litigation route. It forwards the grievance to the company and may take up to 30 days. More than 2,000 companies take part in the Convergence programme. Source: [National Consumer Helpline - About](https://consumerhelpline.gov.in/public/about), [National Consumer Helpline - Convergence programme](https://consumerhelpline.gov.in/public/convergenceprogram)
- `nch_form_fields` (secondary_only): The grievance form asks: Grievance Type*, Grievance Classification*, Company*, Sector/Industry*, Category*, Nature of Grievance*, Product Value*, Dealer name/address/email/contact (optional, 'for improving the chance of redressal'), Grievance Details*, Purchase District/State*, Expectation*, 'Have you registered your grievance with the company?'*, Documents 1 to 3 (JPG, JPEG, PNG, DOC or PDF, maximum 5 MB each, no double extensions) and a declaration of truth. Drafts auto-save. The dropdown options were not captured. Source: [NCH Grievance Registration Form, screenshots captured by the team afte](https://consumerhelpline.gov.in/user/register-complaint.php), [National Consumer Helpline - Sign-up page (7 mandatory account fields)](https://consumerhelpline.gov.in/user/signup.php)
- `brand_first` (product_decision): Product rule: the user always contacts the brand or seller first. The NCH form itself asks whether the grievance was registered with the company. Source: [Team decision recorded in the Country Pack India review answers, 10 Oc](https://github.com/), [NCH Grievance Registration Form, screenshots captured by the team afte](https://consumerhelpline.gov.in/user/register-complaint.php)

**NCH form map:**

| Form field | Required | Filled from |
|---|---|---|
| grievance_type | yes | Pick from the list. Hint: complaint. |
| grievance_classification | yes | Pick from the list. |
| company | yes | brand (If the brand is not listed, select Other and type it.) |
| sector_industry | yes | Pick the sector for the product type. |
| category | yes | Pick from the list. |
| nature_of_grievance | yes | Pick from the list. Hint: defective product. |
| product_value | yes | price_inr |
| dealer_details | no | seller_name, seller_address, seller_email, seller_phone (Optional, but it improves the chance of redressal.) |
| grievance_details | yes | body |
| purchase_district_state | yes | purchase_district, purchase_state |
| expectation | yes | remedy_requested |
| registered_with_company | yes | Answer Yes. The company's complaint number goes in the details text. |
| documents | no | Up to 3 files, JPG, JPEG, PNG, DOC or PDF, 5 MB each, no double extension. Suggest: invoice, warranty card, one photo or the company's reply. |

### English

```text
Company: {brand}. Product: {product}, model {model}, serial {serial}.
Bought on {purchase_date} for Rs {price_inr}, invoice {invoice_no}.
Problem: {defect_statement}, since {fault_first_seen}.
Registered with the company: yes, on {brand_complaint_date}, complaint number {brand_complaint_no}. Their response: {brand_response}.
What I want: {remedy_requested}.
I have the invoice, warranty card and photos and can share them.
```

### हिन्दी

```text
कंपनी: {brand}। उत्पाद: {product}, मॉडल {model}, सीरियल {serial}।
{purchase_date} को {price_inr} रुपये में खरीदा, बिल नंबर {invoice_no}।
समस्या: {defect_statement}, {fault_first_seen} से।
कंपनी में दर्ज: हाँ, {brand_complaint_date} को, शिकायत नंबर {brand_complaint_no}। कंपनी का जवाब: {brand_response}।
मेरी माँग: {remedy_requested}।
मेरे पास बिल, वारंटी कार्ड और फ़ोटो हैं और ज़रूरत पड़ने पर भेजे जा सकते हैं।
```

## 4. Notice before filing a consumer complaint (sent by the consumer)
*उपभोक्ता शिकायत से पहले नोटिस (उपभोक्ता द्वारा भेजा गया)*

`notice_before_complaint`

**Note:** A step in Covered's flow: the app asks you to send this before it prepares the complaint, and to wait out the days you chose. It is not a lawyer's legal notice. The law does not require it as far as we found (rule no_notice_required_before_filing, unverified), so never say it is a legal duty. Send it by registered post or email and keep the proof of delivery. It does not stop the 2-year limit, which counts from the purchase date, so send it early. notice_days is your own choice. The app fills forum_name from the price paid.

**Note (hi):** Covered की प्रक्रिया का एक चरण: शिकायत तैयार करने से पहले ऐप आपसे यह नोटिस भेजने और आपके चुने दिनों तक इंतज़ार करने को कहता है। यह वकील का कानूनी नोटिस नहीं है। हमारी जानकारी में कानून इसे अनिवार्य नहीं करता (नियम no_notice_required_before_filing, असत्यापित), इसलिए इसे कभी कानूनी ज़िम्मेदारी न बताएँ। इसे रजिस्टर्ड डाक या ईमेल से भेजें और भेजने का प्रमाण रखें। इससे 2 साल की समय-सीमा नहीं रुकती, जो खरीद की तारीख से गिनी जाती है, इसलिए इसे जल्दी भेजें। notice_days आपकी अपनी पसंद है। forum_name ऐप चुकाई गई कीमत से भरता है।

**Legal basis (rule, verification, source):**

- `no_notice_required_before_filing` (unverified): Negative finding: no provision found that requires a consumer to send a notice before filing. Covered still makes the notice a required step in its own flow (rule notice_step_in_flow); it never tells the user the law requires it. Regulation 10 of the Procedure Regulations concerns notice issued by the Commission after filing. Not proven by a full-text search. Source: [CPA 2019 s.35 Manner in which complaint shall be made (AdvocateKhoj)](https://www.advocatekhoj.com/library/bareacts/consumerprotection2019/35.php?Title=Consumer+Protection+Act%2C+2019&STitle=Manner+in+which+complaint+shall+be+made), [Consumer Commission Procedure Regulations, 2020 (Taxguru; reg. 7 copie](https://taxguru.in/corporate-law/consumer-protection-consumer-commission-procedure-regulations-2020.html)
- `notice_step_in_flow` (product_decision): Product rule: Covered always asks the user to send the notice before it prepares the complaint, and to wait out the reply period they chose. It is dated evidence that the other side had a chance to act. It is a Covered step, not a legal duty, and it does not stop the two-year limit counted from purchase, so the app tells the user to send it early. Source: [Team decision recorded in the Country Pack India review answers, 10 Oc](https://github.com/), [A self-filed e-Jagriti case (forum post): notarised affidavit, hard co](https://techenclave.com/t/i-filed-a-consumer-court-case-against-flipkart-by-myself-through-e-jagriti/440667)
- `defect_definition` (secondary_only): Defect: any fault, imperfection or shortcoming in quality, quantity, potency, purity or standard required by law, by contract (express or implied) or as claimed by the trader. CPA 2019 s.2(10). A breakdown alone does not prove a statutory defect. Source: [CPA 2019 s.2 Definitions (AdvocateKhoj)](https://www.advocatekhoj.com/library/bareacts/consumerprotection2019/2.php?Title=Consumer+Protection+Act%2C+2019&STitle=Definitions), [CPA 2019 s.2 Definitions (consumerprotection.in), clause cross-check](https://www.consumerprotection.in/section-2-definitions/), [Consumer Protection Act, 2019 - PRS India reproduction (text ends befo](https://PRSINDIA.org/files/bills_acts/bills_parliament/2021/Consumer%20Protection%20Act%202019.pdf), [Consumer Protection Act, 2019 - India Code record (text not opened by ](https://www.indiacode.nic.in/handle/123456789/15256)
- `limitation_two_years` (secondary_only): A complaint must be filed within two years from the date the cause of action arose. A Commission may admit a late complaint for sufficient cause, with reasons recorded. CPA 2019 s.69. Source: [CPA 2019 s.69 Limitation period (consumerprotection.in)](https://www.consumerprotection.in/section-69-limitation-period/), [Consumer Protection Act, 2019 - PRS India reproduction (text ends befo](https://PRSINDIA.org/files/bills_acts/bills_parliament/2021/Consumer%20Protection%20Act%202019.pdf)
- `limitation_counted_from_purchase` (product_decision): Product rule: the app counts the two years from the date of purchase. s.69 counts from the date the cause of action arose, which for a fault that appears later can be later than the purchase date. Counting from purchase is the cautious reading: it never tells a user they have more time than the Act allows, but it can tell a user with a late-arising cause of action that time has run out when a Commission might still hear them. The limitation_passed message says so. A lawyer should confirm before release. Source: [Team decision recorded in the Country Pack India review answers, 10 Oc](https://github.com/), [CPA 2019 s.69 Limitation period (consumerprotection.in)](https://www.consumerprotection.in/section-69-limitation-period/)
- `district_pecuniary_limit` (primary_checked): District Commission: value of goods or services paid as consideration up to Rs 50 lakh (rule 3). State Commission: above Rs 50 lakh up to Rs 2 crore (rule 4). National Commission: above Rs 2 crore (rule 5). G.S.R. 912(E), 30 Dec 2021. Source: [Consumer Protection (Jurisdiction of the District Commission, the Stat](https://www.thc.nic.in/Central%20Governmental%20Rules/Consumer%20Protection%20(Jurisdiction%20of%20the%20District%20Commission,%20the%20State%20Commission%20and%20the%20National%20Commission)%20Rules,%202021.pdf)

### English

```text
Date: {date}

From: {user_name}, {user_address}

To:
1. {brand}, {brand_address}
2. {seller_name}, {seller_address}

Subject: Notice before filing a consumer complaint - defective {product}, model {model}, serial {serial}

1. On {purchase_date} I bought the above product for Rs {price_inr} (invoice {invoice_no}).
2. The product has the following fault, which first appeared on {fault_first_seen}: {defect_statement}.
3. I reported it as follows, without a resolution: {timeline_of_complaints}.
4. I request you to {remedy_requested} within {notice_days} days of receiving this notice.
5. If you do not, I intend to file a complaint before the {forum_name} under the Consumer Protection Act, 2019, seeking the reliefs available under that Act, without further notice.

{user_name}
```

### हिन्दी

```text
दिनांक: {date}

प्रेषक: {user_name}, {user_address}

सेवा में:
1. {brand}, {brand_address}
2. {seller_name}, {seller_address}

विषय: उपभोक्ता शिकायत दर्ज करने से पहले नोटिस - खराब {product}, मॉडल {model}, सीरियल {serial}

1. मैंने {purchase_date} को उपर्युक्त उत्पाद {price_inr} रुपये में खरीदा (बिल नंबर {invoice_no})।
2. उत्पाद में यह खराबी है, जो पहली बार {fault_first_seen} को आई: {defect_statement}।
3. मैंने इसकी शिकायत इस प्रकार की, पर समाधान नहीं हुआ: {timeline_of_complaints}।
4. अनुरोध है कि यह नोटिस प्राप्त होने के {notice_days} दिनों के भीतर {remedy_requested}।
5. ऐसा न होने पर, बिना और नोटिस दिए, उपभोक्ता संरक्षण अधिनियम, 2019 के तहत {forum_name} में शिकायत दर्ज कराई जाएगी और उस अधिनियम में उपलब्ध राहतें माँगी जाएँगी।

{user_name}
```

## 5. Complaint before the District Consumer Disputes Redressal Commission
*ज़िला उपभोक्ता विवाद निवारण आयोग (District Commission) के समक्ष शिकायत*

`district_commission_complaint`

**Note:** For goods priced up to Rs 50 lakh. Above that the app shows the State or National Commission message and no template (MVP). Used for the e-Jagriti 'Proforma' upload; that reading is an assumption. The app drops empty slots and numbers the grounds and the reliefs. Keep only the grounds that match the case. Annexure labels A-1, A-2 follow a first-hand filing report and are unconfirmed. Hindi pleading terms differ by state; use the term on the state commission's own site if it differs. A District Commission may not accept Hindi; check before filing.

**Note (hi):** 50 लाख रुपये तक की कीमत के सामान के लिए। इससे ऊपर ऐप राज्य या राष्ट्रीय आयोग का संदेश दिखाता है, टेम्पलेट नहीं (MVP)। e-Jagriti के 'Proforma' अपलोड के लिए प्रयुक्त; यह पढ़ना एक अनुमान है। ऐप खाली स्लॉट हटाकर आधार और राहतों को क्रम-संख्या देता है। केवल वे आधार रखें जो मामले पर लागू हों। अनुलग्नक के नाम A-1, A-2 एक उपभोक्ता की दायर प्रक्रिया की रिपोर्ट पर आधारित हैं और अपुष्ट हैं। हिंदी में पदों के रूप राज्य के अनुसार बदलते हैं; राज्य आयोग की अपनी साइट का शब्द अलग हो तो वही लें। ज़िला आयोग हिंदी स्वीकार न करे, यह संभव है; दाखिल करने से पहले पूछ लें।

**Legal basis (rule, verification, source):**

- `consumer_definition` (secondary_only): A consumer buys goods for consideration, offline or online, not for resale or a commercial purpose. CPA 2019 s.2(7). Source: [CPA 2019 s.2 Definitions (AdvocateKhoj)](https://www.advocatekhoj.com/library/bareacts/consumerprotection2019/2.php?Title=Consumer+Protection+Act%2C+2019&STitle=Definitions)
- `defect_definition` (secondary_only): Defect: any fault, imperfection or shortcoming in quality, quantity, potency, purity or standard required by law, by contract (express or implied) or as claimed by the trader. CPA 2019 s.2(10). A breakdown alone does not prove a statutory defect. Source: [CPA 2019 s.2 Definitions (AdvocateKhoj)](https://www.advocatekhoj.com/library/bareacts/consumerprotection2019/2.php?Title=Consumer+Protection+Act%2C+2019&STitle=Definitions), [CPA 2019 s.2 Definitions (consumerprotection.in), clause cross-check](https://www.consumerprotection.in/section-2-definitions/), [Consumer Protection Act, 2019 - PRS India reproduction (text ends befo](https://PRSINDIA.org/files/bills_acts/bills_parliament/2021/Consumer%20Protection%20Act%202019.pdf), [Consumer Protection Act, 2019 - India Code record (text not opened by ](https://www.indiacode.nic.in/handle/123456789/15256)
- `deficiency_is_for_services` (secondary_only): Deficiency applies to services, for example a service centre's repair work. CPA 2019 s.2(11). Keep it conditional; do not apply it to every faulty product. Source: [CPA 2019 s.2 Definitions (AdvocateKhoj)](https://www.advocatekhoj.com/library/bareacts/consumerprotection2019/2.php?Title=Consumer+Protection+Act%2C+2019&STitle=Definitions), [Consumer Protection Act, 2019 - PRS India reproduction (text ends befo](https://PRSINDIA.org/files/bills_acts/bills_parliament/2021/Consumer%20Protection%20Act%202019.pdf)
- `utp_refuse_defective_return` (secondary_only): Refusing to take back defective goods and refund the price within the period stated on the bill, or otherwise thirty days, is an unfair trade practice. CPA 2019 s.2(47)(viii). The text does not say when the thirty days start. It is not a general return right or warranty period. No template may state a start date. Source: [CPA 2019 s.2 Definitions (AdvocateKhoj)](https://www.advocatekhoj.com/library/bareacts/consumerprotection2019/2.php?Title=Consumer+Protection+Act%2C+2019&STitle=Definitions), [CPA 2019 s.2 Definitions (consumerprotection.in), clause cross-check](https://www.consumerprotection.in/section-2-definitions/), [Consumer Protection Act, 2019 - PRS India reproduction (text ends befo](https://PRSINDIA.org/files/bills_acts/bills_parliament/2021/Consumer%20Protection%20Act%202019.pdf)
- `utp_no_bill` (secondary_only): Not issuing a bill, cash memo or receipt is an unfair trade practice. CPA 2019 s.2(47)(vii). Source: [CPA 2019 s.2 Definitions (AdvocateKhoj)](https://www.advocatekhoj.com/library/bareacts/consumerprotection2019/2.php?Title=Consumer+Protection+Act%2C+2019&STitle=Definitions), [CPA 2019 s.2 Definitions (consumerprotection.in), clause cross-check](https://www.consumerprotection.in/section-2-definitions/), [Consumer Protection Act, 2019 - PRS India reproduction (text ends befo](https://PRSINDIA.org/files/bills_acts/bills_parliament/2021/Consumer%20Protection%20Act%202019.pdf)
- `district_pecuniary_limit` (primary_checked): District Commission: value of goods or services paid as consideration up to Rs 50 lakh (rule 3). State Commission: above Rs 50 lakh up to Rs 2 crore (rule 4). National Commission: above Rs 2 crore (rule 5). G.S.R. 912(E), 30 Dec 2021. Source: [Consumer Protection (Jurisdiction of the District Commission, the Stat](https://www.thc.nic.in/Central%20Governmental%20Rules/Consumer%20Protection%20(Jurisdiction%20of%20the%20District%20Commission,%20the%20State%20Commission%20and%20the%20National%20Commission)%20Rules,%202021.pdf)
- `act_s34_1_text_differs` (secondary_only): The Act's own s.34(1) still reads Rs 1 crore for the District Commission. The 2021 Rules prescribe Rs 50 lakh. Use the Rules. Source: [Consumer Protection Act, 2019 - PRS India reproduction (text ends befo](https://PRSINDIA.org/files/bills_acts/bills_parliament/2021/Consumer%20Protection%20Act%202019.pdf), [Consumer Protection (Jurisdiction of the District Commission, the Stat](https://www.thc.nic.in/Central%20Governmental%20Rules/Consumer%20Protection%20(Jurisdiction%20of%20the%20District%20Commission,%20the%20State%20Commission%20and%20the%20National%20Commission)%20Rules,%202021.pdf)
- `territorial_complainant_residence` (secondary_only): A complaint may be filed where the opposite party lives or carries on business, where the cause of action arose wholly or in part, or where the complainant lives or works for gain. CPA 2019 s.34(2). Source: [CPA 2019 s.34 Jurisdiction of District Commission (AdvocateKhoj)](https://www.advocatekhoj.com/library/bareacts/consumerprotection2019/34.php?Title=Consumer+Protection+Act%2C+2019&STitle=Jurisdiction+of+District+Commission), [Consumer Protection Act, 2019 - PRS India reproduction (text ends befo](https://PRSINDIA.org/files/bills_acts/bills_parliament/2021/Consumer%20Protection%20Act%202019.pdf)
- `limitation_two_years` (secondary_only): A complaint must be filed within two years from the date the cause of action arose. A Commission may admit a late complaint for sufficient cause, with reasons recorded. CPA 2019 s.69. Source: [CPA 2019 s.69 Limitation period (consumerprotection.in)](https://www.consumerprotection.in/section-69-limitation-period/), [Consumer Protection Act, 2019 - PRS India reproduction (text ends befo](https://PRSINDIA.org/files/bills_acts/bills_parliament/2021/Consumer%20Protection%20Act%202019.pdf)
- `limitation_counted_from_purchase` (product_decision): Product rule: the app counts the two years from the date of purchase. s.69 counts from the date the cause of action arose, which for a fault that appears later can be later than the purchase date. Counting from purchase is the cautious reading: it never tells a user they have more time than the Act allows, but it can tell a user with a late-arising cause of action that time has run out when a Commission might still hear them. The limitation_passed message says so. A lawyer should confirm before release. Source: [Team decision recorded in the Country Pack India review answers, 10 Oc](https://github.com/), [CPA 2019 s.69 Limitation period (consumerprotection.in)](https://www.consumerprotection.in/section-69-limitation-period/)
- `fee_table_rule7` (primary_checked): Fee by value of goods or services paid as consideration: up to Rs 5 lakh Nil; above 5 and up to 10 lakh Rs 200; above 10 and up to 20 lakh Rs 400; above 20 and up to 50 lakh Rs 1,000; above 50 lakh and up to 1 crore Rs 2,000; above 1 and up to 2 crore Rs 2,500; and higher slabs for the National Commission. Rule 7(2) as substituted by G.S.R. 606(E), 17 Aug 2023. The table has no commission column; commission follows the value limits in district_pecuniary_limit. Source: [Consumer Protection (Consumer Disputes Redressal Commissions) Amendmen](https://egazette.gov.in/WriteReadData/2023/248158.pdf)
- `reliefs_available` (secondary_only): Reliefs, CPA 2019 s.39(1): (a) remove a defect pointed out by the appropriate laboratory; (b) replace with defect-free goods; (c) return the price with interest; (d) compensation for loss or injury due to negligence (punitive damages are a proviso to (d)); (e) compensation in a product liability action; (f) remove defects in goods or deficiencies in services; (g) stop the unfair trade practice and not repeat it; (m) adequate costs. Defect removal in a template cites (f), not (a). A second-model review on 9 Oct 2026 mapped (a) to defect removal and (f) to a welfare fund; two readings of the text disagree with it. Source: [CPA 2019 s.39 Findings of District Commission (AdvocateKhoj), clauses ](https://www.advocatekhoj.com/library/bareacts/consumerprotection2019/39.php?Title=Consumer+Protection+Act%2C+2019&STitle=Findings+of+District+Commission), [Consumer Protection Act, 2019 - PRS India reproduction (text ends befo](https://PRSINDIA.org/files/bills_acts/bills_parliament/2021/Consumer%20Protection%20Act%202019.pdf)
- `who_can_file` (secondary_only): The consumer, a recognised consumer association, or other persons named in s.35 may file. Filing may be electronic. CPA 2019 s.35. The text read does not mention a prior notice, an affidavit or a language. Source: [CPA 2019 s.35 Manner in which complaint shall be made (AdvocateKhoj)](https://www.advocatekhoj.com/library/bareacts/consumerprotection2019/35.php?Title=Consumer+Protection+Act%2C+2019&STitle=Manner+in+which+complaint+shall+be+made), [Consumer Protection Act, 2019 - PRS India reproduction (text ends befo](https://PRSINDIA.org/files/bills_acts/bills_parliament/2021/Consumer%20Protection%20Act%202019.pdf)
- `ejagriti_is_the_portal` (primary_checked): e-Jagriti (e-jagriti.gov.in) is the online system for filing and tracking consumer cases; live 1 Jan 2025; replaced e-Daakhil. Source: [PIB: e-Jagriti revolutionizes consumer justice (16 Nov 2025)](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190535&reg=48&lang=2)
- `language_scope_mvp` (product_decision): Product rule: the MVP supports English and Hindi. Formal filings default to English with a Hindi copy. Whether a District Commission accepts a Hindi complaint is state-specific and unverified. Other languages are later. Source: [Team decision recorded in the Country Pack India review answers, 10 Oc](https://github.com/), [Consumer Commission Procedure Regulations, 2020 (Taxguru; reg. 7 copie](https://taxguru.in/corporate-law/consumer-protection-consumer-commission-procedure-regulations-2020.html)

**Slots** (the app drops empty slots and picks the option that fits):

- `{warranty_fact}`: Pick by the coverage result. Never use an assumed warranty in a filing.
  - `in_warranty`: The warranty runs until {warranty_until}, counted from {warranty_start_text} (Annexure A-2).
    - हिन्दी: वारंटी {warranty_until} तक है, जो {warranty_start_text} से गिनी गई है (अनुलग्नक A-2)।
  - `ended`: The warranty ended on {warranty_until} (Annexure A-2). The fault first appeared on {fault_first_seen}.
    - हिन्दी: वारंटी {warranty_until} को समाप्त हुई (अनुलग्नक A-2)। खराबी पहली बार {fault_first_seen} को आई थी।
- `{technician_fact}`: Team proposal. Only when a written report from an authorised service centre exists.
  - `present`: An authorised service centre recorded in writing that {technician_finding} (Annexure A-5).
    - हिन्दी: अधिकृत सर्विस सेंटर ने लिखित में दर्ज किया कि {technician_finding} (अनुलग्नक A-5)।
- `{notice_fact}`: Covered's flow requires the notice first. Drop only if the user skipped it.
  - `sent`: The Complainant sent a written notice to the Opposite Parties on {notice_date} and allowed {notice_days} days to respond (Annexure A-6). Their response: {outcome_so_far}
    - हिन्दी: शिकायतकर्ता ने {notice_date} को विपक्षी पक्षों को लिखित नोटिस भेजा और जवाब के लिए {notice_days} दिन दिए (अनुलग्नक A-6)। उनका जवाब: {outcome_so_far}
- `{ground_defect}`: Always.
  - `always`: The fault is a defect within the meaning of section 2(10) of the Act.
    - हिन्दी: यह खराबी अधिनियम की धारा 2(10) के अर्थ में दोष (defect) है।
- `{ground_deficiency}`: Only if a service centre or seller failed in repair or service.
  - `present`: The failure to repair the product properly is a deficiency in service within the meaning of section 2(11).
    - हिन्दी: उत्पाद की ठीक से मरम्मत न करना धारा 2(11) के अर्थ में सेवा में कमी (deficiency in service) है।
- `{ground_return}`: Only if the seller refused to take back the defective goods and refund the price.
  - `present`: Opposite Party 2 refused on {refusal_date} to take back the defective goods and refund the price within the period stated on the bill or, where none is stated, within thirty days. This is an unfair trade practice under section 2(47)(viii).
    - हिन्दी: विपक्षी पक्ष 2 ने {refusal_date} को बिल पर लिखी अवधि के भीतर, या अवधि न लिखी हो तो तीस दिन के भीतर, दोषपूर्ण सामान वापस लेने और कीमत लौटाने से मना कर दिया। यह धारा 2(47)(viii) के तहत अनुचित व्यापार प्रथा (unfair trade practice) है।
- `{ground_bill}`: Only if no bill, cash memo or receipt was issued.
  - `present`: Not issuing a bill, cash memo or receipt is an unfair trade practice under section 2(47)(vii).
    - हिन्दी: बिल, कैश मेमो या रसीद न देना धारा 2(47)(vii) के तहत अनुचित व्यापार प्रथा (unfair trade practice) है।
- `{territorial_basis}`: Pick the basis that applies. Section 34(2).
  - `residence`: The Complainant resides or personally works for gain within the territorial jurisdiction of this Commission (section 34(2)).
    - हिन्दी: शिकायतकर्ता इस आयोग के क्षेत्र में निवास करता है या स्वयं लाभ के लिए काम करता है (धारा 34(2))।
  - `opposite_party`: An Opposite Party resides or carries on business within the territorial jurisdiction of this Commission (section 34(2)).
    - हिन्दी: कोई विपक्षी पक्ष इस आयोग के क्षेत्र में रहता है या कारोबार करता है (धारा 34(2))।
  - `cause_of_action`: The cause of action arose, wholly or in part, within the territorial jurisdiction of this Commission (section 34(2)).
    - हिन्दी: वाद-कारण (cause of action) पूरा या आंशिक रूप से इस आयोग के क्षेत्र में उत्पन्न हुआ (धारा 34(2))।
- `{limitation_line}`: Pick by the limitation result. The two years are counted from the date of purchase (product rule, the cautious reading of s.69).
  - `within`: This complaint is filed within two years of the date of purchase, and therefore within two years of the cause of action (section 69).
    - हिन्दी: यह शिकायत खरीद की तारीख से दो वर्ष के भीतर, और इसलिए वाद-कारण (cause of action) से भी दो वर्ष के भीतर, दाखिल की जा रही है (धारा 69)।
  - `condonation`: This complaint is filed more than two years after the date of purchase. An application for condonation of delay, stating sufficient cause, is filed with it (section 69).
    - हिन्दी: यह शिकायत खरीद की तारीख से दो वर्ष से अधिक बाद दाखिल की जा रही है। देरी माफ़ी (condonation of delay) का आवेदन, पर्याप्त कारण बताते हुए, साथ में दाखिल है (धारा 69)।
- `{fee_statement}`: Filled by the app from price_inr using the fee table in country.yaml.
  - `nil`: The value of the goods paid is up to Rs 5 lakh; no fee is payable.
    - हिन्दी: चुकाए गए सामान का मूल्य 5 लाख रुपये तक है; कोई फ़ीस देय नहीं है।
  - `amount`: The fee of Rs {fee_inr} prescribed for goods valued at Rs {price_inr} has been paid.
    - हिन्दी: मूल्य {price_inr} रुपये के सामान के लिए निर्धारित {fee_inr} रुपये की फ़ीस जमा की गई है।
- `{relief_list}`: The user picks one or more. Section 39(1) clause in brackets is for the team, not printed in the complaint.
  - `remove_defect` [39(1)(f)]: remove the defect in the product, free of cost;
    - हिन्दी: उत्पाद का दोष निःशुल्क दूर करें;
  - `replace` [39(1)(b)]: replace the product with a new product of the same description, free from defect;
    - हिन्दी: उत्पाद को उसी विवरण के नए, दोष-मुक्त उत्पाद से बदलें;
  - `refund` [39(1)(c)]: return the price of Rs {price_inr}, with interest as the Commission decides;
    - हिन्दी: कीमत {price_inr} रुपये, आयोग द्वारा तय ब्याज सहित, लौटाएँ;
  - `compensation` [39(1)(d)]: pay compensation of Rs {compensation_inr} for the loss and injury suffered;
    - हिन्दी: हुई हानि और क्षति के लिए {compensation_inr} रुपये मुआवज़ा (compensation) दें;
  - `stop_utp` [39(1)(g)]: discontinue the unfair trade practice and not repeat it;
    - हिन्दी: अनुचित व्यापार प्रथा बंद करें और उसे दोहराएँ नहीं;
  - `costs` [39(1)(m)]: pay Rs {costs_inr} as the costs of this proceeding.
    - हिन्दी: इस कार्यवाही के खर्च (costs) के रूप में {costs_inr} रुपये दें।

### English

```text
BEFORE THE DISTRICT CONSUMER DISPUTES REDRESSAL COMMISSION, {district}, {state}

Consumer Complaint No. ______ of ______

IN THE MATTER OF:
{user_name}, aged {user_age}, {user_relation_line}, resident of {user_address}. Phone {user_phone}, email {user_email}.
... Complainant

VERSUS

1. {op1_name}, {op1_address} (manufacturer)
2. {op2_name}, {op2_address} (seller)
3. {op3_name}, {op3_address} (authorised service centre, if any)
... Opposite Parties

COMPLAINT UNDER SECTION 35 OF THE CONSUMER PROTECTION ACT, 2019

A. SYNOPSIS AND LIST OF DATES
Filed separately; see pages {pg_synopsis}.

B. FACTS
1. The Complainant bought a {product}, model {model}, serial {serial}, from Opposite Party 2 on {purchase_date} for Rs {price_inr}, invoice {invoice_no} (Annexure A-1). The Complainant bought it for personal use and is a consumer under section 2(7).
2. {warranty_fact}
3. The product developed the following fault, which first appeared on {fault_first_seen}: {defect_statement} (photographs, Annexure A-3).
4. The Complainant approached the Opposite Parties as follows (Annexure A-4): {timeline_of_complaints}
5. {deficiency_facts}
6. {technician_fact}
7. {notice_fact}

C. GROUNDS
1. {ground_defect}
2. {ground_deficiency}
3. {ground_return}
4. {ground_bill}

D. JURISDICTION, LIMITATION AND FEE
1. The value of the goods paid as consideration is Rs {price_inr}, which is within the pecuniary jurisdiction of this Commission.
2. {territorial_basis}
3. The cause of action arose when the fault first appeared on {fault_first_seen}, and continued when {cause_of_action_facts}. {limitation_line}
4. {fee_statement}

E. RELIEF
The Complainant prays that this Commission direct the Opposite Parties to:
{relief_list}

VERIFICATION
Verified by me, {user_name}, the Complainant, that the contents of this complaint are true and correct to my knowledge and belief, and that nothing material has been concealed.

Place: {place}
Date: {date}
Signature of the Complainant

LIST OF ANNEXURES
{annexure_list}
```

### हिन्दी

```text
ज़िला उपभोक्ता विवाद निवारण आयोग (District Consumer Disputes Redressal Commission), {district}, {state} के समक्ष

उपभोक्ता शिकायत संख्या ______ वर्ष ______

मामला:
{user_name}, आयु {user_age}, {user_relation_line}, निवासी {user_address}। फ़ोन {user_phone}, ईमेल {user_email}।
... शिकायतकर्ता (Complainant)

बनाम

1. {op1_name}, {op1_address} (निर्माता)
2. {op2_name}, {op2_address} (विक्रेता)
3. {op3_name}, {op3_address} (अधिकृत सर्विस सेंटर, यदि हो)
... विपक्षी पक्ष (Opposite Parties)

उपभोक्ता संरक्षण अधिनियम, 2019 की धारा 35 के अंतर्गत शिकायत

क. सार और तारीखों की सूची (Synopsis and List of Dates)
अलग से दाखिल; पृष्ठ {pg_synopsis} देखें।

ख. तथ्य
1. शिकायतकर्ता ने विपक्षी पक्ष 2 से {purchase_date} को {product}, मॉडल {model}, सीरियल {serial}, {price_inr} रुपये में खरीदा, बिल नंबर {invoice_no} (अनुलग्नक A-1)। शिकायतकर्ता ने इसे निजी उपयोग के लिए खरीदा और धारा 2(7) के तहत उपभोक्ता है।
2. {warranty_fact}
3. उत्पाद में यह खराबी आई, जो पहली बार {fault_first_seen} को दिखी: {defect_statement} (फ़ोटो, अनुलग्नक A-3)।
4. शिकायतकर्ता ने विपक्षी पक्षों से इस प्रकार संपर्क किया (अनुलग्नक A-4): {timeline_of_complaints}
5. {deficiency_facts}
6. {technician_fact}
7. {notice_fact}

ग. आधार
1. {ground_defect}
2. {ground_deficiency}
3. {ground_return}
4. {ground_bill}

घ. क्षेत्राधिकार, समय-सीमा और फ़ीस
1. चुकाए गए सामान का मूल्य {price_inr} रुपये है, जो इस आयोग के आर्थिक क्षेत्राधिकार (pecuniary jurisdiction) में है।
2. {territorial_basis}
3. वाद-कारण तब उत्पन्न हुआ जब खराबी पहली बार {fault_first_seen} को आई, और तब भी जारी रहा जब {cause_of_action_facts}। {limitation_line}
4. {fee_statement}

ङ. माँगी गई राहत
शिकायतकर्ता की प्रार्थना है कि आयोग विपक्षी पक्षों को निर्देश दे कि वे:
{relief_list}

सत्यापन (Verification)
मुझ, {user_name}, शिकायतकर्ता द्वारा सत्यापित किया जाता है कि इस शिकायत की बातें मेरी जानकारी और विश्वास में सही हैं और कोई महत्वपूर्ण बात छिपाई नहीं गई है।

स्थान: {place}
दिनांक: {date}
शिकायतकर्ता के हस्ताक्षर

अनुलग्नकों की सूची (List of Annexures)
{annexure_list}
```

## 6. Index of documents
*दस्तावेज़ों की अनुक्रमणिका (Index)*

`index`

**Note:** First upload on e-Jagriti. Page numbers are filled after the set is paged. Delete the Vakalatnama row if no advocate is engaged.

**Note (hi):** e-Jagriti पर पहला अपलोड। पृष्ठ संख्या पूरा सेट पन्ने-क्रम में लगाने के बाद भरें। अधिवक्ता न हो तो वकालतनामा की पंक्ति हटा दें।

**Legal basis (rule, verification, source):**

- `ejagriti_documents` (primary_checked): The upload step lists: Index, Proforma, Synopsis, Memo of Parties, Notarized Affidavit, Vakalatnama; then Annexures with a title, or an IA application. File types and size limits are not stated in the manual. Source: [e-Jagriti help manual for consumer complaint filing](https://e-jagriti.gov.in/static/media/CC_Filing.34e0fc5dd03b1d864cab.pdf), [NCDRC complaint proforma (model only)](https://ncdrc.nic.in/images/cc.htm)
- `offline_copies` (secondary_only): Offline filing at a District Commission: three sets plus one per opposite party (Procedure Regulations reg. 7(1)). A first-hand post says printed copies were still needed with numbered pages and annexures labelled A-1, A-2. Source: [Consumer Commission Procedure Regulations, 2020 (Taxguru; reg. 7 copie](https://taxguru.in/corporate-law/consumer-protection-consumer-commission-procedure-regulations-2020.html), [A self-filed e-Jagriti case (forum post): notarised affidavit, hard co](https://techenclave.com/t/i-filed-a-consumer-court-case-against-flipkart-by-myself-through-e-jagriti/440667)

**Slots** (the app drops empty slots and picks the option that fits):

- `{vakalatnama_row}`: Only when the user chose to file through an advocate (routes.filing_mode = advocate).
  - `present`: 6. Vakalatnama
    - हिन्दी: 6. वकालतनामा (Vakalatnama)

### English

```text
BEFORE THE DISTRICT CONSUMER DISPUTES REDRESSAL COMMISSION, {district}, {state}

Consumer Complaint No. ______ of ______
{user_name} ... Complainant   VERSUS   {op1_name} and others ... Opposite Parties

INDEX

S.No.  Particulars                              Page
1.     Index                                    1
2.     Complaint (Proforma)                     {pg_complaint}
3.     Synopsis and List of Dates               {pg_synopsis}
4.     Memo of Parties                          {pg_memo}
5.     Affidavit (notarised)                    {pg_affidavit}
{vakalatnama_row}
7.     Annexures                                see below
{annexure_index_lines}

Place: {place}
Date: {date}
Complainant: {user_name}
```

### हिन्दी

```text
ज़िला उपभोक्ता विवाद निवारण आयोग (District Consumer Disputes Redressal Commission), {district}, {state} के समक्ष

उपभोक्ता शिकायत संख्या ______ वर्ष ______
{user_name} ... शिकायतकर्ता (Complainant)   बनाम   {op1_name} एवं अन्य ... विपक्षी पक्ष (Opposite Parties)

अनुक्रमणिका (Index)

क्र.सं.  विवरण                                    पृष्ठ
1.      अनुक्रमणिका                               1
2.      शिकायत (Proforma)                         {pg_complaint}
3.      सार और तारीखों की सूची                    {pg_synopsis}
4.      पक्षकारों का ज्ञापन                        {pg_memo}
5.      शपथ-पत्र (Affidavit), नोटरी से सत्यापित               {pg_affidavit}
{vakalatnama_row}
7.      अनुलग्नक (Annexures)                      नीचे देखें
{annexure_index_lines}

स्थान: {place}
दिनांक: {date}
शिकायतकर्ता: {user_name}
```

## 7. Synopsis and list of dates
*सार और तारीखों की सूची*

`synopsis_list_of_dates`

**Note:** Short summary plus a dated table. Keep the dates identical to the complaint.

**Note (hi):** संक्षिप्त सार और तारीखों की तालिका। तारीखें शिकायत से मेल खानी चाहिए।

**Legal basis (rule, verification, source):**

- `ejagriti_documents` (primary_checked): The upload step lists: Index, Proforma, Synopsis, Memo of Parties, Notarized Affidavit, Vakalatnama; then Annexures with a title, or an IA application. File types and size limits are not stated in the manual. Source: [e-Jagriti help manual for consumer complaint filing](https://e-jagriti.gov.in/static/media/CC_Filing.34e0fc5dd03b1d864cab.pdf), [NCDRC complaint proforma (model only)](https://ncdrc.nic.in/images/cc.htm)
- `limitation_counted_from_purchase` (product_decision): Product rule: the app counts the two years from the date of purchase. s.69 counts from the date the cause of action arose, which for a fault that appears later can be later than the purchase date. Counting from purchase is the cautious reading: it never tells a user they have more time than the Act allows, but it can tell a user with a late-arising cause of action that time has run out when a Commission might still hear them. The limitation_passed message says so. A lawyer should confirm before release. Source: [Team decision recorded in the Country Pack India review answers, 10 Oc](https://github.com/), [CPA 2019 s.69 Limitation period (consumerprotection.in)](https://www.consumerprotection.in/section-69-limitation-period/)

### English

```text
BEFORE THE DISTRICT CONSUMER DISPUTES REDRESSAL COMMISSION, {district}, {state}

Consumer Complaint No. ______ of ______

SYNOPSIS
1. The Complainant bought a {brand} {product}, model {model}, serial {serial}, on {purchase_date} for Rs {price_inr}.
2. The product developed this fault on {fault_first_seen}: {defect_statement}.
3. The Complainant approached the Opposite Parties: {timeline_of_complaints}. Result: {outcome_so_far}.
4. The Complainant therefore seeks: {relief_summary}.

LIST OF DATES
Date                 Event
{purchase_date}      Purchase of the product (Annexure A-1)
{fault_first_seen}   Fault first appeared
{dated_events}
{filing_date}        Complaint filed

Place: {place}
Complainant: {user_name}
```

### हिन्दी

```text
ज़िला उपभोक्ता विवाद निवारण आयोग (District Consumer Disputes Redressal Commission), {district}, {state} के समक्ष

उपभोक्ता शिकायत संख्या ______ वर्ष ______

सार (Synopsis)
1. शिकायतकर्ता (Complainant) ने {brand} कंपनी का {product}, मॉडल {model}, सीरियल {serial}, {purchase_date} को {price_inr} रुपये में खरीदा।
2. {fault_first_seen} को उत्पाद में यह खराबी आई: {defect_statement}।
3. शिकायतकर्ता ने विपक्षी पक्षों (Opposite Parties) से संपर्क किया: {timeline_of_complaints}। परिणाम: {outcome_so_far}।
4. इसलिए शिकायतकर्ता की माँग है: {relief_summary}।

तारीखों की सूची (List of Dates)
तारीख                घटना
{purchase_date}      उत्पाद की खरीद (अनुलग्नक A-1)
{fault_first_seen}   खराबी पहली बार आई
{dated_events}
{filing_date}        शिकायत दाखिल की गई

स्थान: {place}
शिकायतकर्ता: {user_name}
```

## 8. Memo of parties
*पक्षकारों का ज्ञापन (Memo of Parties)*

`memo_of_parties`

**Note:** Names and addresses of all parties, with phone and email so the Commission can serve notice.

**Note (hi):** सभी पक्षकारों के नाम और पते, फ़ोन और ईमेल सहित, ताकि आयोग नोटिस भेज सके।

**Legal basis (rule, verification, source):**

- `ejagriti_documents` (primary_checked): The upload step lists: Index, Proforma, Synopsis, Memo of Parties, Notarized Affidavit, Vakalatnama; then Annexures with a title, or an IA application. File types and size limits are not stated in the manual. Source: [e-Jagriti help manual for consumer complaint filing](https://e-jagriti.gov.in/static/media/CC_Filing.34e0fc5dd03b1d864cab.pdf), [NCDRC complaint proforma (model only)](https://ncdrc.nic.in/images/cc.htm)
- `who_can_file` (secondary_only): The consumer, a recognised consumer association, or other persons named in s.35 may file. Filing may be electronic. CPA 2019 s.35. The text read does not mention a prior notice, an affidavit or a language. Source: [CPA 2019 s.35 Manner in which complaint shall be made (AdvocateKhoj)](https://www.advocatekhoj.com/library/bareacts/consumerprotection2019/35.php?Title=Consumer+Protection+Act%2C+2019&STitle=Manner+in+which+complaint+shall+be+made), [Consumer Protection Act, 2019 - PRS India reproduction (text ends befo](https://PRSINDIA.org/files/bills_acts/bills_parliament/2021/Consumer%20Protection%20Act%202019.pdf)

### English

```text
BEFORE THE DISTRICT CONSUMER DISPUTES REDRESSAL COMMISSION, {district}, {state}

Consumer Complaint No. ______ of ______

MEMO OF PARTIES

{user_name}, aged {user_age}, {user_relation_line}
Resident of {user_address}
Phone {user_phone}, email {user_email}
... Complainant

VERSUS

1. {op1_name}
   {op1_address}
   (manufacturer)
2. {op2_name}
   {op2_address}
   (seller)
3. {op3_name}
   {op3_address}
   (authorised service centre, if any)
... Opposite Parties

Place: {place}
Date: {date}
Complainant: {user_name}
```

### हिन्दी

```text
ज़िला उपभोक्ता विवाद निवारण आयोग (District Consumer Disputes Redressal Commission), {district}, {state} के समक्ष

उपभोक्ता शिकायत संख्या ______ वर्ष ______

पक्षकारों का ज्ञापन (Memo of Parties)

{user_name}, आयु {user_age}, {user_relation_line}
निवासी {user_address}
फ़ोन {user_phone}, ईमेल {user_email}
... शिकायतकर्ता (Complainant)

बनाम

1. {op1_name}
   {op1_address}
   (निर्माता)
2. {op2_name}
   {op2_address}
   (विक्रेता)
3. {op3_name}
   {op3_address}
   (अधिकृत सर्विस सेंटर, यदि हो)
... विपक्षी पक्ष (Opposite Parties)

स्थान: {place}
दिनांक: {date}
शिकायतकर्ता: {user_name}
```

## 9. Affidavit in support of the complaint (to be notarised)
*शिकायत के समर्थन में शपथ-पत्र (Affidavit), नोटरी से सत्यापित कराने के लिए*

`affidavit`

**Note:** Treated as required: the e-Jagriti manual lists a Notarized Affidavit. Print it, sign it before a notary, and scan it. The notary completes the last block. Whether stamp paper is needed, and the notary's fee, vary by place; one first-hand post reports Rs 200. Not verified.

**Note (hi):** अनिवार्य माना गया है: e-Jagriti की मैनुअल में नोटरी से सत्यापित शपथ-पत्र (Notarized Affidavit) अपलोड की सूची में है। इसे प्रिंट करें, नोटरी के सामने हस्ताक्षर करें और स्कैन करें। अंतिम खंड नोटरी भरते हैं। स्टाम्प पेपर चाहिए या नहीं और नोटरी की फ़ीस जगह के अनुसार बदलती है; एक उपभोक्ता की पोस्ट में 200 रुपये बताए गए हैं। असत्यापित।

**Legal basis (rule, verification, source):**

- `ejagriti_documents` (primary_checked): The upload step lists: Index, Proforma, Synopsis, Memo of Parties, Notarized Affidavit, Vakalatnama; then Annexures with a title, or an IA application. File types and size limits are not stated in the manual. Source: [e-Jagriti help manual for consumer complaint filing](https://e-jagriti.gov.in/static/media/CC_Filing.34e0fc5dd03b1d864cab.pdf), [NCDRC complaint proforma (model only)](https://ncdrc.nic.in/images/cc.htm)
- `ejagriti_affidavit_notarised` (primary_checked): Treat a notarised affidavit as required. The manual lists it as an upload; one first-hand post says it cost Rs 200 and was redone after the wrong commission was selected. The Act text and Procedure Regulations summary read do not mention it. Source: [e-Jagriti help manual for consumer complaint filing](https://e-jagriti.gov.in/static/media/CC_Filing.34e0fc5dd03b1d864cab.pdf), [A self-filed e-Jagriti case (forum post): notarised affidavit, hard co](https://techenclave.com/t/i-filed-a-consumer-court-case-against-flipkart-by-myself-through-e-jagriti/440667)

### English

```text
BEFORE THE DISTRICT CONSUMER DISPUTES REDRESSAL COMMISSION, {district}, {state}

Consumer Complaint No. ______ of ______
{user_name} ... Complainant   VERSUS   {op1_name} and others ... Opposite Parties

AFFIDAVIT

I, {user_name}, aged {user_age}, {user_relation_line}, resident of {user_address}, do solemnly affirm and state as follows:

1. I am the Complainant in the above complaint and am competent to swear this affidavit.
2. I have read the accompanying complaint. The contents of paragraphs {fact_paras} are true and correct to my knowledge, and the rest are true and correct to my belief. Nothing material has been concealed.
3. The annexures filed with the complaint are true copies of the documents in my possession.

DEPONENT

VERIFICATION
Verified at {place} on {date} that the contents of this affidavit are true and correct to my knowledge and belief, that nothing in it is false, and that nothing material has been concealed.

DEPONENT

(To be completed by the Notary: sworn or affirmed before me on ______ at ______. Notary's name, registration number, seal and signature.)
```

### हिन्दी

```text
ज़िला उपभोक्ता विवाद निवारण आयोग (District Consumer Disputes Redressal Commission), {district}, {state} के समक्ष

उपभोक्ता शिकायत संख्या ______ वर्ष ______
{user_name} ... शिकायतकर्ता (Complainant)   बनाम   {op1_name} एवं अन्य ... विपक्षी पक्ष (Opposite Parties)

शपथ-पत्र (Affidavit)

शपथकर्ता (Deponent) {user_name}, आयु {user_age}, {user_relation_line}, निवासी {user_address}, का शपथपूर्वक कथन:

1. शपथकर्ता उपर्युक्त शिकायत में शिकायतकर्ता है और यह शपथ-पत्र देने में सक्षम है।
2. संलग्न शिकायत पढ़ी जा चुकी है। पैराग्राफ़ {fact_paras} की बातें शपथकर्ता की जानकारी में सही हैं, और शेष बातें शपथकर्ता के विश्वास में सही हैं। कोई महत्वपूर्ण बात छिपाई नहीं गई है।
3. शिकायत के साथ दाखिल अनुलग्नक शपथकर्ता के पास मौजूद मूल कागज़ों की सही प्रतियाँ हैं।

शपथकर्ता

सत्यापन (Verification)
{place} में {date} को सत्यापित किया जाता है कि इस शपथ-पत्र की बातें शपथकर्ता की जानकारी और विश्वास में सही हैं, इसमें कुछ भी झूठा नहीं है और कोई महत्वपूर्ण बात छिपाई नहीं गई है।

शपथकर्ता

(नोटरी द्वारा भरा जाए: मेरे समक्ष ______ को ______ में शपथ ली गई या दृढ़ कथन किया गया। नोटरी का नाम, पंजीकरण संख्या, मुहर और हस्ताक्षर।)
```

## Field catalog

| Field | English label | हिन्दी | Kind |
|---|---|---|---|
| `date` | Date | दिनांक | date |
| `place` | Place | स्थान | text |
| `filing_date` | Date of filing | दाखिल करने की तारीख | date |
| `user_name` | Your full name | आपका पूरा नाम | text |
| `user_address` | Your address | आपका पता | text |
| `user_phone` | Your phone | आपका फ़ोन | text |
| `user_email` | Your email | आपका ईमेल | text |
| `user_age` | Your age | आपकी आयु | number |
| `user_relation_line` | Relation line, e.g. son of Shri X, daughter of Shri X, wife of Shri X | संबंध की पंक्ति, जैसे पुत्र श्री क, पुत्री श्री क, पत्नी श्री क | text |
| `brand` | Brand | ब्रांड | text |
| `brand_address` | Brand's registered or service address | ब्रांड का पंजीकृत या सर्विस पता | text |
| `seller_name` | Seller's name | विक्रेता का नाम | text |
| `seller_address` | Seller's address | विक्रेता का पता | text |
| `seller_email` | Seller's email | विक्रेता का ईमेल | text |
| `seller_phone` | Seller's phone | विक्रेता का फ़ोन | text |
| `product` | Product | उत्पाद | text |
| `model` | Model | मॉडल | text |
| `serial` | Serial number | सीरियल नंबर | text |
| `invoice_no` | Invoice number | बिल नंबर | text |
| `purchase_date` | Purchase date | खरीद की तारीख | date |
| `price_inr` | Price paid, in rupees | चुकाई गई कीमत, रुपये में | number |
| `warranty_until` | Warranty end date | वारंटी समाप्ति की तारीख | date |
| `warranty_start_text` | Warranty start (purchase date or installation date) | वारंटी की शुरुआत (खरीद की तारीख या इंस्टॉलेशन की तारीख) | text |
| `warranty_source_text` | Where the warranty terms came from (warranty card, brand website, Right to Repair portal) | वारंटी की शर्तें कहाँ से लीं (वारंटी कार्ड, कंपनी की वेबसाइट, राइट टू रिपेयर पोर्टल) | text |
| `imei` | IMEI (phones) | IMEI (फ़ोन के लिए) | text |
| `installation_date` | Installation date | इंस्टॉलेशन की तारीख | date |
| `product_registration_no` | Product registration number | उत्पाद पंजीकरण संख्या | text |
| `defect_statement` | What is wrong with the product | उत्पाद में क्या खराबी है | text |
| `fault_first_seen` | Date the fault first appeared | खराबी पहली बार कब आई (तारीख) | date |
| `defect_reason` | Why you think it is a manufacturing defect | आपको यह निर्माण-दोष क्यों लगता है | text |
| `technician_finding` | What the authorised service centre wrote about the cause | अधिकृत सर्विस सेंटर ने कारण के बारे में क्या लिखा | text |
| `steps_tried` | Basic checks you tried | आपने कौन-सी बुनियादी जाँचें कीं | text |
| `service_requests` | Earlier service requests, with numbers and dates | पहले की सर्विस शिकायतें, नंबर और तारीख सहित | text |
| `service_request_no` | Latest service request number | सबसे ताज़ा सर्विस शिकायत नंबर | text |
| `gap_statement` | What is still unresolved and what the company has not done | क्या अब भी हल नहीं हुआ और कंपनी ने क्या नहीं किया | text |
| `remedy_requested` | What you ask for, as an action, e.g. repair the product, replace it, refund the price | आप क्या चाहते हैं, कार्य के रूप में, जैसे उत्पाद की मरम्मत करें, बदलें, कीमत लौटाएँ | text |
| `reply_days` | Days you allow for a reply (your own deadline; Covered suggests 15) | जवाब के लिए आपके दिए दिन (आपकी अपनी समय-सीमा; Covered 15 सुझाता है) | number |
| `extra_attachments` | Other attachments | अन्य संलग्न कागज़ | text |
| `plan_provider` | Plan provider or card issuer | प्लान देने वाली कंपनी या कार्ड जारी करने वाला बैंक | text |
| `plan_number` | Plan number | प्लान नंबर | text |
| `plan_valid_until` | Plan valid until | प्लान की मान्यता तक | date |
| `card_name` | Card name | कार्ड का नाम | text |
| `card_benefit_name` | Name of the card benefit, as the issuer calls it | कार्ड के लाभ का नाम, जैसा जारीकर्ता बताता है | text |
| `brand_complaint_date` | Date you complained to the company | कंपनी से शिकायत की तारीख | date |
| `brand_complaint_no` | Company's complaint number | कंपनी का शिकायत नंबर | text |
| `brand_response` | What the company answered | कंपनी ने क्या जवाब दिया | text |
| `purchase_district` | District of purchase | खरीद का ज़िला | text |
| `purchase_state` | State of purchase | खरीद का राज्य | text |
| `timeline_of_complaints` | How and when you reported it, and what happened | आपने कब और कैसे शिकायत की, और क्या हुआ | text |
| `notice_date` | Date you sent the notice | नोटिस भेजने की तारीख | date |
| `notice_days` | Days you give in the notice (your choice; Covered suggests 15) | नोटिस में दिए गए दिन (आपकी पसंद; Covered 15 सुझाता है) | number |
| `forum_name` | Commission that has jurisdiction, filled by the app from the price | अधिकार-क्षेत्र वाला आयोग, कीमत के आधार पर ऐप भरता है | derived |
| `district` | District of the Commission | आयोग का ज़िला | text |
| `state` | State | राज्य | text |
| `op1_name` | Opposite Party 1 (manufacturer): name | विपक्षी पक्ष 1 (निर्माता): नाम | text |
| `op1_address` | Opposite Party 1: address | विपक्षी पक्ष 1: पता | text |
| `op2_name` | Opposite Party 2 (seller): name | विपक्षी पक्ष 2 (विक्रेता): नाम | text |
| `op2_address` | Opposite Party 2: address | विपक्षी पक्ष 2: पता | text |
| `op3_name` | Opposite Party 3 (authorised service centre, if any): name | विपक्षी पक्ष 3 (अधिकृत सर्विस सेंटर, यदि हो): नाम | text |
| `op3_address` | Opposite Party 3: address | विपक्षी पक्ष 3: पता | text |
| `deficiency_facts` | Facts about the service centre's or seller's failures | सर्विस सेंटर या विक्रेता की चूक के तथ्य | text |
| `refusal_date` | Date the seller refused to take the goods back | विक्रेता ने सामान वापस लेने से मना किया, वह तारीख | date |
| `cause_of_action_facts` | What the Opposite Parties did or refused to do | विपक्षी पक्षों ने क्या किया या करने से मना किया | text |
| `fee_inr` | Filing fee in rupees, filled by the app from the price | दाखिल करने की फ़ीस, कीमत के आधार पर ऐप भरता है | derived |
| `compensation_inr` | Compensation you ask for, in rupees | आप जितना मुआवज़ा माँगते हैं, रुपये में | number |
| `costs_inr` | Costs of the proceeding you ask for, in rupees | कार्यवाही के खर्च की माँग, रुपये में | number |
| `relief_summary` | Short list of reliefs sought | माँगी गई राहतों की संक्षिप्त सूची | text |
| `outcome_so_far` | What the Opposite Parties answered or did | विपक्षी पक्षों ने क्या जवाब दिया या किया | text |
| `dated_events` | Other dated events, one per line: date - event | अन्य तारीख वाली घटनाएँ, हर पंक्ति में: तारीख - घटना | text |
| `annexure_list` | List of annexures with titles | अनुलग्नकों की सूची, शीर्षक सहित | text |
| `annexure_index_lines` | Annexures with page numbers | पृष्ठ संख्या सहित अनुलग्नक | text |
| `pg_complaint` | Pages of the complaint | शिकायत के पृष्ठ | text |
| `pg_synopsis` | Pages of the synopsis | सार के पृष्ठ | text |
| `pg_memo` | Pages of the memo of parties | पक्षकारों के ज्ञापन के पृष्ठ | text |
| `pg_affidavit` | Pages of the affidavit | शपथ-पत्र के पृष्ठ | text |
| `fact_paras` | Paragraph numbers of the complaint the affidavit covers | शिकायत के जिन पैराग्राफ़ पर शपथ-पत्र है उनके नंबर | text |
