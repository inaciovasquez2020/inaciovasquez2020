# Contributing to the Profile README Surface

This repository is the profile-level start-here map and routing surface for the URF repository network.

## Contribution classes

### 1. Documentation improvements

- clarify start-here wording
- improve onboarding text
- improve routing descriptions across the README and docs
- fix broken or ambiguous references

### 2. Verification hardening

- improve repository checks
- tighten documentation/test consistency
- strengthen profile-surface navigation guarantees

### 3. Scope or authority changes

These require explicit justification.

- changing repository-role declarations
- changing canonical routing language
- changing status or authority statements
- expanding scope claims

## Preferred workflow

```bash
git fetch origin --prune
git switch main
git pull --ff-only origin main
git switch -c your-branch-name
```

Run repository checks before commit:

```bash
python3 -m pytest -q
```

Then commit:

```bash
git add <files>
git commit -m "docs: improve onboarding surface"
git push -u origin your-branch-name
```

## Disallowed without explicit justification

- silent semantic changes
- changing profile-authority language without synchronized documentation updates
- expanding scope or status claims without updating the public routing surfaces
