# Setup Guide

This guide is for contributors who want a reliable local environment for the profile/overview routing surface.

## Prerequisites

```bash
python3 --version
git --version
```

Recommended baseline:

- Python 3.10 or newer
- Git
- POSIX shell environment

## Clone

```bash
git clone https://github.com/inaciovasquez2020/inaciovasquez2020.git
cd inaciovasquez2020
```

## Optional virtual environment

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install --upgrade pip
```

## Verification

```bash
python3 -m pytest -q
```

## Recommended edit loop

```bash
git pull --ff-only origin main
python3 -m pytest -q
git status --short
```

## Related files

- `QUICKSTART.md`
- `CONTRIBUTING.md`
- `README.md`
- `docs/`
- `artifacts/`
- `tests/`
