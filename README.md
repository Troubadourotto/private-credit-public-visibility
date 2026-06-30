# Public Visibility of Valuation Markdown Events in BDC-Held Private Credit Loans

This repository contains a pilot data-construction and research-design project on public information opacity in private credit markets.

## Research question

When BDC-held private credit loans experience valuation markdowns, are borrower-specific deterioration signals publicly visible to outside investors?

This is **not** framed as a prediction model and does **not** claim that public news causes private credit valuation marks. Public information is used as an outside-investor visibility screen.

## Project positioning

This project is intended as a **pilot research-design project**, not a completed empirical paper. Its main purpose is to demonstrate a feasible research design for studying information opacity in private credit markets using public BDC disclosures.

The emphasis is on:

- constructing a source-traceable borrower-level valuation panel from BDC Schedule of Investments disclosures;
- defining transparent markdown-event rules;
- applying a conservative public-visibility coding framework; and
- showing how the pilot can be scaled into a broader research agenda on information opacity and credit-risk discovery in private debt markets.

A useful way to read this project is: **BDC valuation marks may provide a public window into otherwise opaque private credit exposures; the project asks whether those marks reveal borrower-level deterioration that outside investors could not easily observe from borrower-specific public sources.**

## What this project does not claim

This project does **not** claim that:

- BDCs intentionally delay markdowns;
- public news causes private credit valuation changes;
- public signals predict private credit marks;
- the 15-observation pilot sample represents the full private credit market; or
- a `no clear public signal found` code proves that no public information existed.

The project uses public information only as a visibility screen for an outside investor.

## Project motivation

Private credit borrowers are often private companies with limited public reporting. BDC Schedule of Investments disclosures provide one of the few recurring public sources of borrower-level fair value marks. This project asks whether visible markdowns in BDC filings are accompanied by public borrower-specific deterioration signals, or whether the markdowns reveal information that is difficult to observe publicly.

## Sample construction protocol

The sample is hand-collected and selected for **source traceability and clean borrower-level matching**, not for representativeness. The protocol is:

1. Select large publicly traded BDCs with detailed Schedule of Investments disclosures.
2. Use Q4 2025 and Q1 2026 filings so that borrower rows can be compared across adjacent reporting dates.
3. Identify borrowers that can be matched across both quarters with reasonably clear legal-name or borrower-name continuity.
4. Aggregate multiple first-lien rows at the borrower level when the rows correspond to the same borrower exposure.
5. Exclude or avoid cases where borrower identity, facility mapping, or source rows are too ambiguous for a pilot audit trail.
6. Lock the valuation sample before coding the public visibility layer, so that public-source search results do not determine sample inclusion.

The resulting sample has 15 borrower-level observations across ARCC, BXSL, and OBDC.

## Key outputs

- [Research note PDF](docs/public_visibility_research_note.pdf)
- [Methodology note](docs/public_visibility_methodology.md)
- [Filing source tracker](data/source_tracker/filing_sources.csv)
- [Borrower row source tracker](data/source_tracker/borrower_row_sources.csv)
- [Combined valuation panel](data/processed/bdc_combined_valuation_panel_completed.csv)
- [Public visibility coding file](data/raw_manual/public_signal_layer_v2.csv)
- [Summary table](output/valuation_signal_summary.csv)
- [RA research brief](docs/ra_research_brief.md)
- [RA email blurb and CV bullet](docs/ra_email_blurb.md)
- [Validation and summary code](code/01_validate_and_summarize_bdc_panel.py)

The research note is the best entry point for understanding the project motivation, data construction, pilot findings, limitations, and future extension. The RA research brief is a shorter version intended for outreach or pre-doc/RA applications.

## Reproducibility

The repository includes a simple Python validation script. From the repository root, run:

```bash
python code/01_validate_and_summarize_bdc_panel.py
```

The script recalculates valuation ratios and markdown flags, checks that the stored variables match the calculations, merges the public-visibility coding layer, and regenerates the summary table, markdown-case table, signal crosstab, and figures.

## Data

The pilot sample contains 15 borrower-level observations across three publicly traded BDCs:

- Ares Capital Corporation (ARCC)
- Blackstone Secured Lending Fund (BXSL)
- Blue Owl Capital Corporation (OBDC)

The valuation panel tracks Q4 2025 to Q1 2026 changes in fair value-to-cost or fair value-to-amortized-cost ratios, depending on the wording used in each BDC schedule. BXSL and OBDC source schedules report amounts in thousands; the processed panel converts these values to $mm for consistency with the ARCC panel.

## Source traceability

The repo includes two source-tracking files:

- `data/source_tracker/filing_sources.csv` identifies the filing, accession number, SEC archive URL, source unit, and schedule used for each BDC.
- `data/source_tracker/borrower_row_sources.csv` records borrower-level row matching and aggregation notes used to construct each observation.

This source-tracking layer is intended to make the hand-coded pilot easier to audit and extend.

## Event definitions

- `fair_value_to_cost = fair_value / cost_or_amortized_cost`
- `level_markdown_event = 1` if `fair_value_to_cost < 0.90`
- `qoq_markdown_event = 1` if `Q1 FV/cost - Q4 FV/cost < -0.05`

The -5 percentage-point QoQ threshold is a pilot coding rule rather than a statistical cutoff. Threshold sensitivity is reported in the summary file.

Important measurement caveat: quarter-over-quarter changes in this ratio are borrower-level valuation-mark proxies, not pure same-loan revaluation effects. Borrower observations may include multiple facilities and may be affected by draws, repayments, PIK/accretion, amortized-cost changes, or facility mix changes.

## Public visibility coding

Public signal strength is coded as:

| Code | Meaning |
|---:|---|
| 0 | No clear public signal found |
| 1 | Industry/comparable weak signal |
| 2 | Borrower-specific soft deterioration signal |
| 3 | Borrower-specific hard credit/distress signal |

A public signal must be observable, dated, negative or risk-increasing, and plausibly related to borrower credit quality, operating condition, or recovery value. Signals are also tagged for whether they were observable by the Q1 valuation date.

## Pilot findings

| Metric | Count |
|---|---:|
| Total observations | 15 |
| Q4 level markdown events | 6 |
| Q1 level markdown events | 8 |
| QoQ markdown events at -5pp threshold | 4 |
| QoQ markdown events at -7.5pp threshold | 2 |
| QoQ markdown events at -10pp threshold | 1 |
| Borrower-specific hard credit/distress signals | 0 |
| Borrower-specific soft signals | 2 |
| Industry/comparable weak signals | 8 |
| No clear public signal found | 5 |
| Broad public signals, any timing | 10 |
| Broad public signals observable by Q1 valuation date | 9 |

The main comparison is the QoQ markdown subsample. Among the 4 quarter-over-quarter markdown cases, none has a clear borrower-specific hard-credit public signal in the current hand-coded review. Three cases have pre-Q1 industry or comparable-company public context, and one has no clear public signal.

The broad 10/15 public-signal count is reported for transparency, but it should not be interpreted as borrower-specific evidence. Most of these signals are industry/comparable context rather than direct borrower-level deterioration.

## Interpretation

The main contribution of this pilot is not a causal claim. The project shows a feasible way to construct a borrower-level BDC valuation panel and compare valuation marks with a conservative public information screen. The early finding is consistent with the idea that borrower-level credit deterioration in private credit can be difficult for outside investors to observe using public information alone.

## Broader research agenda

This pilot points to a broader research agenda on **how borrower-level credit deterioration becomes visible in opaque private debt markets**. BDC disclosures are useful because they provide repeated, borrower-level fair value marks for private credit exposures that usually do not have public financial statements, traded debt prices, or equity-market signals. The central research idea is that BDC valuation marks may reveal credit-risk information that outside investors cannot easily infer from borrower-specific public sources.

In that sense, the project is not only a small descriptive exercise. It is a feasibility test for a larger study of **information opacity, credit-risk discovery, and valuation disclosure in private debt markets**.

## Future extension

A larger extension would scale this pilot across publicly traded BDCs and multiple reporting quarters, build a larger event panel of borrower-level valuation-mark proxies, and classify whether markdown events are preceded by borrower-specific public signals, industry/comparable signals, or no observable public signal. A larger study could then examine whether BDC valuation marks reveal borrower-level deterioration before it appears through later public events such as non-accrual status, restructurings, bankruptcy filings, rating actions, or other credit outcomes.

This extension would move the project from a hand-coded pilot toward a broader empirical question: **when and through which channels does credit deterioration in private debt markets become visible to outside investors?**

## Repository structure

```text
├── code/
│   └── 01_validate_and_summarize_bdc_panel.py
├── data/
│   ├── processed/
│   │   ├── bdc_combined_valuation_panel_completed.csv
│   │   └── bdc_combined_valuation_panel_completed.xlsx
│   ├── raw_manual/
│   │   ├── public_signal_layer_v2.csv
│   │   └── public_signal_layer_v2.xlsx
│   └── source_tracker/
│       ├── borrower_row_sources.csv
│       ├── filing_sources.csv
│       └── source_tracker.xlsx
├── docs/
│   ├── project_overview.md
│   ├── public_visibility_methodology.md
│   ├── public_visibility_research_note.md
│   ├── public_visibility_research_note.docx
│   ├── public_visibility_research_note.pdf
│   ├── ra_email_blurb.md
│   └── ra_research_brief.md
├── output/
│   ├── figures/
│   │   ├── q4_q1_fv_cost_scatter.png
│   │   └── qoq_markdown_signal_visibility.png
│   ├── tables/
│   │   ├── loan_level_panel_summary.csv
│   │   ├── public_signal_crosstab.csv
│   │   └── qoq_markdown_cases.csv
│   └── valuation_signal_summary.csv
├── requirements.txt
└── README.md
```

## Limitations

This is a small, hand-coded pilot sample. It is not designed for statistical inference, causal testing, or prediction. The sample is selected for source traceability rather than representativeness. Public visibility coding is limited by private-company opacity, borrower legal-name mapping, source availability, and source quality. A `no clear public signal found` classification means no clear signal was identified in the current hand-coded review; it should not be read as proof that no public information existed. One QoQ markdown case is close to the -5pp cutoff, so markdown counts should be interpreted as rule-based pilot classifications rather than robust statistical events.

## Next-step research agenda

A larger version can extend the sample to more BDCs, more reporting quarters, and multiple markdown thresholds. A scaled version could systematically collect public-source signals, add industry controls, and link valuation marks to subsequent borrower outcomes such as non-accrual status, restructurings, or bankruptcy filings. The broader research question is whether BDC valuation marks reveal borrower-level deterioration before it becomes visible in other public information channels.

## Code sample

Run `python code/01_validate_and_summarize_bdc_panel.py` from the repository root to validate the valuation variables and regenerate summary outputs.
