# Public Visibility Methodology

## Research design

This project treats public information as an outside-investor visibility screen. It does not assume that public news causes BDC valuation marks. Instead, it asks whether borrower-specific deterioration is publicly observable around BDC valuation markdown events.

The broader research motivation is to study how credit-risk information becomes visible in opaque private debt markets. BDC Schedule of Investments disclosures provide repeated borrower-level fair value marks for private credit exposures, making them a useful public window into otherwise private borrower-credit conditions.

## Sample construction protocol

The sample is hand-collected and selected for source traceability and clean borrower-level matching, not representativeness. The protocol is:

1. Select large publicly traded BDCs with detailed Schedule of Investments disclosures.
2. Use Q4 2025 and Q1 2026 filings to compare adjacent reporting dates.
3. Identify borrowers that can be matched across both quarters with clear legal-name or borrower-name continuity.
4. Aggregate multiple first-lien rows at the borrower level when the rows correspond to the same borrower exposure.
5. Avoid observations where borrower identity, facility mapping, or source rows are too ambiguous for a pilot audit trail.
6. Lock the valuation sample before coding public visibility signals.

This design minimizes post-hoc selection based on whether a public signal is easy to find.

## Valuation panel

The valuation panel is built from BDC Schedule of Investments disclosures for Q4 2025 and Q1 2026. Each row is a borrower-level observation. When the same borrower appears in multiple first-lien rows, rows are aggregated at the borrower level to keep the comparison aligned across quarters. Because borrower-level observations may include multiple facilities and may change through draws, repayments, PIK/accretion, amortized-cost changes, or facility mix changes, quarter-over-quarter changes in fair value-to-cost should be interpreted as borrower-level valuation-mark proxies rather than pure same-loan revaluation effects.

Source traceability is documented in:

- `data/source_tracker/filing_sources.csv`
- `data/source_tracker/borrower_row_sources.csv`

ARCC values are source-normalized to the comparative Dec. 31, 2025 schedule included in the ARCC Q1 2026 filing. BXSL and OBDC values are converted from source units of $000 to processed units of $mm.

## Markdown definitions

- `fair_value_to_cost = fair value / cost or amortized cost`
- `level_markdown_event = 1` if `fair_value_to_cost < 0.90`
- `qoq_markdown_event = 1` if `Q1 FV/cost - Q4 FV/cost < -0.05`

The -5pp QoQ cutoff is a transparent pilot rule. It is not intended to be a statistically estimated threshold. The output summary also reports sensitivity at -7.5pp and -10pp thresholds, and flags cases close to the -5pp cutoff.

## Public visibility coding

A public signal must be publicly observable, dated, negative or risk-increasing, and plausibly related to borrower credit quality, operating condition, or recovery value.

Signal strength:

- 0 = no clear public signal found
- 1 = industry/comparable weak signal
- 2 = borrower-specific soft deterioration signal
- 3 = borrower-specific hard credit/distress signal

Signal timing:

- `pre_q4` = before Dec. 31, 2025
- `between_q4_q1` = Jan. 1, 2026 to Mar. 31, 2026
- `post_q1` = after Mar. 31, 2026
- `none` = no signal found

The column `pre_q1_observable` indicates whether the signal was publicly observable by the Q1 valuation date. This distinction prevents post-Q1 information from being interpreted as evidence available to outside investors before the Q1 mark.

## Interpretation rules

- Industry or comparable-company deterioration is not treated as borrower-specific evidence.
- If no clear source-traceable signal is found, the observation is coded as no clear public signal rather than forced into a narrative. This code means the current hand-coded review did not identify a clear signal; it is not proof that no public information existed.
- Low-strength sources such as Wikipedia are treated only as background mapping/context and not as core evidence for the main finding.
- The project does not use private emails, private messages, internal lender materials, or unpublished internship information.
- Findings should be stated in visibility/opacity language rather than causal prediction language.

## What the project does not claim

The project does not claim that BDCs delay marks, that public news predicts private credit marks, that public information causes valuation changes, or that the pilot sample represents the full private credit market.

## Main pilot comparison

Among the 4 QoQ markdown cases, the hand-coded review finds:

- 0 with a borrower-specific hard credit/distress signal,
- 0 with a borrower-specific soft deterioration signal,
- 3 with only pre-Q1 industry/comparable weak public context,
- 1 with no clear public signal.

This means the core result should be framed as limited public borrower-level visibility rather than evidence that public signals explain or predict markdowns.

## Broader research agenda

The larger agenda is to study how borrower-level deterioration becomes visible in opaque private debt markets. BDC valuation marks can be treated as one public disclosure channel. Public borrower news, industry/comparable information, ratings, restructurings, bankruptcies, or non-accrual disclosures can be treated as alternative visibility channels.

A scaled design would compare the timing of these channels. The scaled-study question is whether BDC marks reveal credit deterioration before it becomes visible through other public information sources.

## Future extension

A larger version would expand the sample across more BDCs and quarters, build an event panel of borrower-level valuation-mark proxies, apply systematic public-source collection, and link markdown events to subsequent credit outcomes such as non-accrual status, restructuring, bankruptcy, rating actions, or distressed exchanges. This would transform the pilot into a broader empirical study of information opacity and credit-risk discovery in private debt markets.
