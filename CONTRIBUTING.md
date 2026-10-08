# Contributing to Covered

## Working together

1. Clone the repository and read `README.md`.
2. Create a branch from the latest `main`: `git switch -c feature/short-description` (use `fix/` for fixes).
3. Make focused changes and verify the behavior you changed. Document relevant checks in the pull request.
4. Commit with a descriptive message and push your branch: `git push -u origin HEAD`.
5. Open a pull request against `main` and request a teammate's review.
6. Resolve feedback before merging. Prefer squash merges, then delete the completed branch.

Use issues to agree on scope and ownership before starting larger changes. Keep `main` usable; avoid pushing directly to it. This workflow is a team convention until repository rules enforce it.

## Secrets and setup

Copy `.env.example` to `.env` when environment settings are needed. Never commit credentials, tokens, or production data. Document new settings in `.env.example` using placeholder values.

The project has no selected language, framework, or test command yet. Add setup and validation instructions when the stack is chosen.
