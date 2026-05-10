# Inácio F. Vasquez

Independent researcher building the Unified Rigidity Framework (URF): a verification-first research program connecting rigidity, locality, entropy, formal proof surfaces, and executable status infrastructure across mathematics, computer science, and physics.

## Start here

- Public front door: https://github.com/inaciovasquez2020/vasquez-index
- Core reference: https://github.com/inaciovasquez2020/urf-core
- Reference implementation: https://github.com/inaciovasquez2020/chronos-urf-rr
- Exposition: https://github.com/inaciovasquez2020/urf-textbook

## What URF is

URF is a repository-governed framework for separating verified structure, conditional reductions, executable certificates, and open frontiers.

## What URF is not

URF is not presented as theorem-level closure of P vs NP, Yang--Mills, Poincare, Navier--Stokes, or any other major open problem unless a repository explicitly states and verifies that claim.

## Current status

| Class | Meaning |
|---|---|
| Verified | Repository checks, CI, Lean/Python/TypeScript verification, and stated certificates pass. |
| Conditional | A result depends on explicitly named assumptions or external theorem inputs. |
| Open | A frontier object remains unresolved. |
| Not claimed | Build success, dashboard status, or executable evidence does not imply theorem-level closure. |

## Repository dependency map

    vasquez-index
       |
       +-- urf-core
       |      |
       |      +-- chronos-urf-rr
       |      +-- CorrRank
       |      +-- overlap-rigidity-lean-dev
       |
       +-- urf-textbook
       |
       +-- applications
       |      +-- biological-friction-framework
       |      +-- ym-os-quantization
       |      +-- poincare-new-derivation
       |
       +-- infrastructure
              +-- frontier-status-dashboard
              +-- non-clay-problem-closure-workspace

## Verification principle

Build PASS means repository verification passed. It does not mean theorem-level closure unless the relevant repository explicitly states and verifies theorem-level closure.

## Links

- ORCID: https://orcid.org/0009-0008-8459-3400
- Research site: https://vasquezresearch.com
- Contact: inacio@vasquezresearch.com

<!-- FRONTIER_STATUS_START -->
## Current public frontier status

Last updated: 2026-05-10

### Chronos / URF-RR

- Selected-domain H4.1/FGL observation-to-gap soundness is closed on `H4_1_FGL_SelectedTheoremDomain`.
- Chronos PR #212 merged and verified: `SELECTED_DOMAIN_GAP_SOUNDNESS_CLOSED`.
- Frontier Status Dashboard PR #41 updated the public Chronos status.
- Frontier Status Dashboard PR #42 hid the private/internal aggregate row from the public dashboard while preserving the guard fixture.

### Public dashboard boundary

- Public dashboard records externally inspectable repositories only.
- Private/internal aggregate metadata is intentionally omitted from the rendered dashboard.
- No unrestricted H4.1/FGL closure is claimed.
- No UniversalFiberEntropyGap theorem is claimed.
- No Chronos-RR theorem closure is claimed.
- No P vs NP or Clay-problem closure is claimed.

### Verification surfaces

- `chronos-urf-rr`: targeted verifier passed, targeted pytest passed, `lake build` passed.
- `frontier-status-dashboard`: `npm test -- --run` passed, `npm run build` passed.
<!-- FRONTIER_STATUS_END -->
