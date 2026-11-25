# Brand

How `lens` presents itself inside the taoque family. This is a decision record, not a
style guide for research content; the research rules live in `references/`.

## Name

`lens`, lowercase, one word. It follows the family pattern of a single lowercase noun
(`trove`, `folio`, `muster`): the product is a thing you pick up, not a category you
describe. Write it lowercase even at the start of a sentence, as the family site does.

Do not reintroduce `MarketLens`, `Market Lens`, `MarketLens Skills`, or a camel-case
variant in prose, page titles, report headers, or package text. The GitHub repository and
clone URL keep the older `marketlens-skills` name until the repository itself is renamed;
that is the only place the old string is allowed.

## One-line job

Turns public filings and market prices into a research label an agent can defend: what the
price implies, whether the earnings are real, and what the evidence allows.

Non-goals, so the identity does not drift:

- Not a data terminal, screener, or live quote feed.
- Not personalized advice or a trade recommendation service.
- Not a replacement for the six skills' evidence rules.

## Mark

`assets/lens-mark.svg` is the source; `assets/lens-mark-small.svg` is the ≤32pt variant.
Both use the family geometry and colors exactly as registered in the taoque skill
(`references/icon.md`, `tokens.json` → `mark`):

| Part | Value |
|---|---|
| Canvas | 128 × 128 |
| Outer tile | `11,11` `106 × 106`, radius 24, stroke 2, paper `#F8F1EA`, edge `#B83D2E` |
| Inner frame | `26,26` `76 × 76`, radius 15, stroke 1.5, `#D6C2B5` |
| Symbol | hand lens, ink `#191514`, stroke 2.5, round caps |
| Accent dot | `(64,102)`, radius 3.5, `#B83D2E` |

The symbol is the product's object: a hand lens, with a three-segment market line inside
the glass. Only the family mark uses a letterform; product marks stay objects.

Small variant: tile plus the lens, symbol stroke 6, no inner frame, no dot.

Exports: `assets/icon-1024.png` (GitHub avatar, mark on paper) and `assets/icon-256.png`
(favicon / site header). SVG is the only source; regenerate the PNGs after any geometry
change and keep the query-string version in step where a surface caches them.

## Voice

- Lead with a verb and a concrete object. No adjective stacks, no "empowers" or
  "one-stop".
- One sentence for the job, then what the six skills share. Repository mechanics
  (runtime, packaging, build) belong below the fold, not in the first paragraph.
- Lowercase wordmark; sentence case for headings.
- Keep the family's single accent. A second colour, a second serif stack, or a second
  mark geometry is out of scope by rule, not by taste.

## Where the identity appears

| Surface | Treatment |
|---|---|
| README (EN / zh-CN) | mark above the wordmark, then the one-line job |
| Typeset examples | `lens` in the header meta and footer; no image mark |
| Reference files | "lens skill", "lens standard" in the opening line |
| Repository | `taoquo/marketlens-skills` until renamed |

## Open items

1. Register the mark in the taoque skill: add `"lens": "marketlens/assets/lens-mark.svg"`
   to `tokens.json` → `mark.products`, then run its `scripts/audit.sh`. The path assumes
   the checkout keeps the `marketlens` directory name; update both together.
2. Rename the GitHub repository to `lens-skills` and update the install command, clone
   URL, and this file's exception note in the same change.
