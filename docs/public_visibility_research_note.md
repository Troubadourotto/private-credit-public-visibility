# Valuation Markdown and Public Information Opacity in BDC-Held Private Credit Loans

**A pilot data-construction and research-design project**  
**Yaoting Bai**

## Abstract

This pilot project constructs a borrower-level valuation panel from BDC Schedule of Investments disclosures and uses public information as an outside-investor visibility screen. The goal is not to claim that public news predicts private credit marks. Instead, the project asks whether borrower-specific deterioration is publicly visible before or around BDC valuation markdowns. In a fixed source-traceable sample of 15 borrower observations from ARCC, BXSL, and OBDC from Q4 2025 to Q1 2026, 4 quarter-over-quarter markdown cases are identified using a -5 percentage-point fair-value-to-cost threshold. None of these markdown cases has a clear borrower-specific hard-credit public signal in the current hand-coded review; 3 have only industry or comparable-company context observable before the Q1 valuation date, and 1 has no clear public signal. The pilot is best interpreted as a feasibility test for studying public visibility and information opacity in private credit, not as a causal or predictive test.

## Research question

When BDC-held private credit loans experience valuation markdowns, are borrower-specific deterioration signals publicly visible to outside investors using public information?

## Motivation

Private credit borrowers are often private companies with limited public reporting. BDC filings provide one of the few recurring public windows into borrower-level fair values. A markdown in a BDC Schedule of Investments may therefore reveal information about borrower credit quality that is not otherwise visible to outside investors. This project uses public information as a visibility screen to ask whether markdown cases are accompanied by observable public deterioration signals.

The broader motivation is credit-risk discovery in opaque private debt markets. If borrower-level deterioration is difficult to observe publicly, then BDC valuation disclosures may serve as one of the first public channels through which outside investors can observe changes in private borrower credit quality.

## What this project does not claim

This project does not claim that BDCs intentionally delay markdowns, that public news causes private credit valuation changes, that public signals predict private credit marks, or that the pilot sample is representative of the full private credit market. It also does not claim that a `no clear public signal found` code proves the absence of public information. The project is a research-design pilot that asks what an outside investor can observe from public sources.

## Sample construction protocol

The sample is selected for source traceability and clean borrower-level matching, not for representativeness. The pilot protocol is:

1. Select large publicly traded BDCs with detailed Schedule of Investments disclosures.
2. Use Q4 2025 and Q1 2026 filings to compare adjacent reporting dates.
3. Identify borrowers that can be matched across both quarters with clear legal-name or borrower-name continuity.
4. Aggregate multiple first-lien rows at the borrower level when the rows correspond to the same borrower exposure.
5. Avoid cases where borrower identity, facility mapping, or source rows are too ambiguous for a pilot audit trail.
6. Lock the valuation sample before coding the public visibility layer, so public-source search results do not determine which borrowers enter the sample.

This protocol produces 15 borrower-level observations across ARCC, BXSL, and OBDC. The resulting dataset is useful for a feasibility test and research-design illustration, but it should not be interpreted as a representative sample of private credit loans.

## Data construction and measurement

The valuation panel uses Schedule of Investments disclosures for ARCC, BXSL, and OBDC. Each row is a borrower-level observation. When multiple first-lien rows correspond to the same borrower, rows are aggregated to maintain borrower-level comparability across Q4 2025 and Q1 2026. The processed valuation panel reports all amounts in $mm. BXSL and OBDC source schedules report amounts in $000, so those values are converted to $mm.

A key measurement caveat is that these are borrower-level valuation-mark proxies rather than pure same-loan revaluation effects. A borrower-level observation may include multiple facilities, changes in facility mix, draws, repayments, PIK/accretion, or amortized-cost changes between quarters. Therefore, the project interprets changes in fair value-to-cost as borrower-level valuation signals from BDC filings, not as proof that an identical loan position was mechanically marked down by the full amount.

The repo includes a filing-level source tracker and borrower-row source tracker to make the data construction auditable. This is important because the project is hand-coded and depends on borrower/facility matching across quarterly schedules.

## Event definitions

The primary valuation measure is:

```text
fair_value_to_cost = fair value / cost or amortized cost
```

The project defines a level markdown event as `fair_value_to_cost < 0.90`. A quarter-over-quarter markdown event is defined as:

```text
Q1 FV/cost - Q4 FV/cost < -0.05
```

The -5pp threshold is a transparent pilot rule. It should not be interpreted as a statistically estimated cutoff. The summary file reports sensitivity at -7.5pp and -10pp thresholds. One markdown case is close to the -5pp cutoff, so event counts should be interpreted as rule-based pilot classifications rather than robust statistical events.

## Public visibility screen

Public signals are coded into four levels:

| Code | Meaning |
|---:|---|
| 0 | No clear public signal found |
| 1 | Industry/comparable weak signal |
| 2 | Borrower-specific soft deterioration signal |
| 3 | Borrower-specific hard credit/distress signal |

A public signal must be observable, dated, negative or risk-increasing, and plausibly related to borrower credit quality, operating condition, or recovery value. Signals are also tagged by timing. The key distinction is whether a signal was observable by the Q1 valuation date. Post-Q1 information is recorded but is not treated as information available before the Q1 mark.

## Pilot findings

- Total observations: 15
- Q4 level markdown events: 6
- Q1 level markdown events: 8
- QoQ markdown events at -5pp threshold: 4
- QoQ markdown events at -7.5pp threshold: 2
- QoQ markdown events at -10pp threshold: 1
- Broad public signals, any timing: 10
- Broad public signals observable by Q1 valuation date: 9
- Borrower-specific hard-credit public signals: 0
- Borrower-specific soft public signals: 2
- Industry/comparable weak signals: 8
- No clear public signal found: 5

The key comparison is the QoQ markdown subsample. Among the 4 quarter-over-quarter markdown cases, none has a borrower-specific hard-credit public signal in the current review. None has a borrower-specific soft signal. Three have only pre-Q1 industry or comparable-company context, and one has no clear public signal.

The broad public-signal count is included for transparency, but it should not be read as borrower-specific evidence. Most identified public context is industry or comparable-company information, which is weaker than direct borrower-level deterioration.

## Interpretation

The project should be interpreted as a public visibility and opacity exercise, not a predictive or causal test. The pilot evidence is consistent with the idea that BDC valuation markdowns may reveal borrower-level deterioration that is difficult for outside investors to detect from public information alone.

The most defensible finding is not that public signals explain markdowns. The stronger interpretation is that obvious borrower-specific hard-credit public signals are limited even among visible markdown cases. This supports the idea that private credit valuation marks may convey information that is not easily observable in public borrower-level sources.

## Broader research agenda

This pilot points to a broader research agenda on how borrower-level credit deterioration becomes visible in opaque private debt markets. BDC valuation disclosures are a useful setting because they provide repeated borrower-level marks for private credit exposures that otherwise lack public financial statements, traded debt prices, or equity-market signals.

The pilot therefore asks a larger question: do BDC valuation marks reveal borrower-level deterioration before outside investors can observe that deterioration through other public channels? Framed this way, the project is not only about the 15 hand-coded observations. It is a feasibility test for studying information opacity, credit-risk discovery, and valuation disclosure in private debt markets.

## Future extension

A larger extension would scale the sample across publicly traded BDCs and multiple reporting quarters, build a larger event panel of borrower-level valuation-mark proxies, and classify whether markdown events are preceded by borrower-specific public signals, industry/comparable signals, or no observable public signal. The larger study could then examine whether BDC valuation marks predict or precede later public credit outcomes such as non-accrual status, restructurings, bankruptcy filings, rating actions, or distressed exchanges.

This extension would move the project from a hand-coded pilot to a broader empirical design around the timing of credit-risk discovery in private debt markets. The central scaled-study question would be: when and through which channels does private borrower deterioration become visible to outside investors?

## Limitations

This is a small, hand-coded pilot sample selected for source traceability, not representativeness. The public visibility screen is limited by private-company opacity, borrower legal-name mapping, paywalled sources, and source quality. Industry or comparable-company signals are weak contextual signals and should not be interpreted as borrower-specific deterioration. A `no clear public signal found` code means that the current public-source review did not identify a clear signal; it is not proof that no public information existed. Borrower-level fair value-to-cost changes should also be interpreted as valuation-mark proxies, because facility composition, draws, repayments, and amortized-cost changes may affect the ratio. The project does not test causality or prediction.

## Next-step research agenda

A larger version of this project could expand to additional BDCs, additional quarters, multiple markdown thresholds, systematic public-source collection, industry controls, and subsequent borrower outcomes such as non-accrual status, restructurings, or bankruptcy filings. The natural extension is an event panel that asks whether BDC valuation marks reveal borrower-level deterioration before it becomes visible in other public information channels. The pilot therefore functions as a research-design seed for studying information opacity and credit-risk discovery in private debt markets.
