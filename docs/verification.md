# Verification Record

lens has two verification layers:

- **Structural** — `scripts/validate_skills.py` checks frontmatter, reference routing,
  output-block order, version consistency, example coverage, and dist parity.
- **Behavioral** — this file records whether the gates actually change an output when they
  should. Structural validation does not prove behavior, and a validator result is never
  evidence that a behavioral scenario passed.

A behavioral scenario is `Pass` only when the expected label, cap, refusal, or block is
visible in the output. Use `Not run` rather than implying coverage.

## How To Run

Structural checks:

```bash
bash scripts/validate-skills.sh
bash scripts/build-skills.sh
REQUIRE_DIST=1 bash scripts/validate-skills.sh
```

Render one example after changing it:

```bash
bash scripts/render-examples.sh examples/lens-v010-valuation-band-nvda.html
```

Behavioral scenarios: run in a fresh session, paste the prompt or fixture, and inspect the
named observable. Record the result in the table below. A scenario that produces the right
label for the wrong reason is `Fail`; state the reason.

## Structural Checks

| Check | Method | Result |
|---|---|---|
| Skill validation | `bash scripts/validate-skills.sh` | Pass — 6 skills |
| Dist parity | `REQUIRE_DIST=1 bash scripts/validate-skills.sh` | Pass |
| Version consistency | validator compares `VERSION`, every `metadata.version`, and the latest `CHANGELOG.md` heading | Pass — 0.12 |
| Example coverage | validator checks both READMEs and `examples/*.html` | Pass — 6 skills, 7 cases |
| README image paths | validator checks every README image reference | Pass |
| Example rendering | `scripts/render-examples.sh` on the changed case | Pass — catalyst case, 2 pages |

## Behavioral Scenarios

| ID | Scenario | Prompt or fixture shape | Expected observable | Status |
|---|---|---|---|---|
| V-01 | Missing decisive source | Ask for a company label; supply only a Tier 3 article, no filing | No label stronger than `monitor closely`; `evidence-gap` if the claim is decisive; the missing Tier 1/2 source is named; the reviewer returns `REVISE` if the draft claims a strong label | Not run |
| V-02 | Missing layer in `full` mode | Ask for a full-chain label with no regime data | Regime is `Unavailable`; the final label is no stronger than `monitor closely`; the missing input is named in `Data Freshness` or `Confidence And Limits` | Not run |
| V-03 | Conflicting layers | Sector is structurally challenged, company quality is A, valuation is cheap | Final label is capped by the sector constraint and names it; no averaged score, no middle-label default | Not run |
| V-04 | Duplicate sources | Supply two vendor copies of one filing as the only support | One source ID; the duplicate copy is not counted as independent support; no source-count padding | Not run |
| V-05 | Stale or undated input | Give a 90-day-old price and no current quote | Freshness is `Lagged` or `Stale`; confidence is capped; no sentence presents the old price as current | Not run |
| V-06 | Missing block or disclaimer | Remove `## Disclaimer` or move `## Data Freshness` after `## Evidence Sources` | Validator fails on block order or disclaimer; a draft review returns `REVISE` | Not run |
| V-07 | Band lacks a usable denominator | Use a 120-observation PE window, or a window with negative TTM earnings | `evidence-gap` or a method switch; no band-based label; the failure boundary is named | Not run |
| V-08 | EPS/PE decomposition | Use price +213%, EPS(TTM) +1,125%, PE -74.4% | Both contributions are reported; the log identity holds within rounding; the text says EPS-led, not a re-rating | Not run |
| V-09 | Red-team failure | Give a strong `add-candidate watch` draft with a credible bear case omitted | Reviewer returns `REVISE` or the label is downgraded; the strongest objection, its layer, and its source are named | Not run |
| V-10 | Unfalsifiable trigger | A draft says `What Would Change The View`: `if fundamentals deteriorate` | Reviewer returns `REVISE`; the trigger is replaced by a metric, threshold, window, direction, and tested layer | Not run |
| V-11 | Separation of duties | Reviewer rewrites the draft; reviser adds an unsourced fact | Protocol violation; the reviewer does not rewrite; the reviser cannot add unsourced facts; the publisher does not repair content | Not run |
| V-12 | Silent failure | A price is 10x the known quote, or a valid ticker returns an empty list | Core figure check records the failure mode; treatment is `Exclude` or `Unavailable`; the empty list is not read as zero or as neutral evidence | Not run |

## Arithmetic Check

The valuation-band decomposition uses `log(price) = log(EPS) + log(PE)`. With the
illustrative example values:

```text
price +213%   -> 3.13x, log = 1.1410
EPS   +1,125% -> 12.25x, log = 2.5055
PE     -74.4% -> 0.256x, log = -1.3626

log(EPS) + log(PE) = 1.1429
rounding gap = 0.0019, or 0.2%
```

Status: `Pass` within the rounding of the published percentages. This checks arithmetic,
not whether the EPS path is reconciled to filings.

## Current Results

| Date | Release | Scope | Result |
|---|---|---|---|
| 2026-11-24 | 0.12 | Structural checks, arithmetic check, P0/P1 protocol, 2026-11-24 example refresh | Structural and arithmetic pass; behavioral scenarios not run |

The behavioral scenarios require a model session and a human or harness judgment. They are
not part of CI, and the validator cannot substitute for them.

## Not Verified

- No automated model-behavior harness runs the scenario matrix. A `Not run` row is a gap,
  not a pass.
- No live market data is used. The examples are illustrative and are not reconciled to
  filings.
- The v0.9 and v0.10 cases were rendered in earlier releases. v0.12 re-renders the catalyst
  case only; the other PDFs and PNGs are unchanged.
- The validator checks structure, not whether a conclusion is correct.
- A full multi-skill run has not been exercised against every host or model. The protocol
  says what should happen; it does not prove that every host follows it.

## Adding A Scenario

Add one row to `## Behavioral Scenarios` with a reproducible prompt, one observable, and a
status. When a scenario fails, record the failure and the fix in the same row; do not delete
the old result. If a scenario becomes deterministic, move it into `scripts/validate_skills.py`
and mark it as structural here.
