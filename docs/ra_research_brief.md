# RA Research Brief

## Public Visibility of Valuation Markdown Events in BDC-Held Private Credit Loans

### Research question

When BDC-held private credit loans experience valuation markdowns, are borrower-specific deterioration signals publicly visible to outside investors?

This pilot studies public information visibility in private credit markets. It does not claim that public news causes private credit valuation changes or that the small pilot sample is representative. Instead, it asks whether visible valuation markdowns in BDC Schedule of Investments disclosures are accompanied by observable borrower-specific public deterioration signals.

### Motivation

Private credit borrowers are often private companies with limited public reporting. BDC filings provide one of the few recurring public windows into borrower-level fair values for private credit exposures. If BDC loan marks change while borrower-specific public deterioration signals are limited or absent, those marks may reveal credit-risk information that outside investors cannot easily observe from public sources alone.

The broader research agenda is information opacity and credit-risk discovery in private debt markets: when and through which channels does private borrower deterioration become visible to outside investors?

### Pilot data

The pilot hand-collects a source-traceable borrower-level valuation panel from three publicly traded BDCs:

- Ares Capital Corporation (ARCC)
- Blackstone Secured Lending Fund (BXSL)
- Blue Owl Capital Corporation (OBDC)

The current sample contains 15 borrower-level observations comparing Q4 2025 and Q1 2026 Schedule of Investments disclosures. The panel tracks cost or amortized cost, fair value, fair value-to-cost, level markdown flags, quarter-over-quarter markdown flags, source pages, and borrower-row construction notes.

### Event definition

The main valuation measure is:

```text
fair value-to-cost = fair value / cost or amortized cost
```

The pilot defines:

- Level markdown event: fair value-to-cost < 0.90
- QoQ markdown event: Q1 fair value-to-cost minus Q4 fair value-to-cost < -0.05

The -5 percentage-point threshold is a transparent pilot rule, not a statistically estimated cutoff. Threshold sensitivity is reported at -7.5pp and -10pp.

### Public visibility screen

Public signals are coded conservatively:

| Code | Meaning |
|---:|---|
| 0 | No clear public signal found |
| 1 | Industry/comparable weak signal |
| 2 | Borrower-specific soft deterioration signal |
| 3 | Borrower-specific hard credit/distress signal |

A signal must be observable, dated, negative or risk-increasing, and plausibly related to borrower credit quality, operating condition, or recovery value. Timing is recorded so that signals observable by the Q1 valuation date can be separated from later information.

### Pilot findings

The pilot sample has 15 observations. At the -5pp QoQ threshold, there are 4 quarter-over-quarter markdown cases. In the current hand-coded review, none of these 4 markdown cases has a clear borrower-specific hard-credit public signal. Three have only pre-Q1 industry or comparable-company context, and one has no clear public signal.

This should not be interpreted as evidence that no public information existed. The finding is more limited: in this small source-traceable pilot, obvious borrower-specific hard-credit signals are not easy to identify even among visible markdown cases.

### Contribution as an RA pilot

This project demonstrates a scalable empirical workflow for studying opaque credit markets:

1. Construct borrower-level BDC valuation panels from Schedule of Investments disclosures.
2. Define transparent loan-markdown event rules.
3. Track source pages and row aggregation decisions.
4. Add a conservative public-information visibility layer.
5. Compare private credit valuation marks with outside-investor public information.

The pilot can be expanded across more BDCs, more quarters, and later credit outcomes such as non-accrual status, restructurings, bankruptcy filings, rating actions, or distressed exchanges.

### Research extension

A larger study could ask whether BDC valuation marks reveal private borrower deterioration before it becomes visible through other public channels. It could also study whether valuation recognition varies across BDCs, loan types, industries, third-party valuation use, or public credit-market stress.

The central scaled-study question is:

**When and through which channels does credit deterioration in private debt markets become visible to outside investors?**
