# Project Overview

This pilot project constructs a borrower-level valuation panel from public BDC Schedule of Investments disclosures and compares valuation-mark proxies with a conservative public-information visibility screen.

The project is framed as a data-construction and research-design exercise. It does not claim that public news causes private credit valuation changes, and it does not attempt to predict valuation marks. Instead, it asks whether borrower-specific deterioration is publicly observable when BDC-held private credit loans experience valuation markdowns.

Key outputs:

- `docs/public_visibility_research_note.pdf` - concise research note.
- `docs/public_visibility_methodology.md` - methodology and coding rules.
- `data/processed/bdc_combined_valuation_panel_completed.csv` - borrower-level valuation panel.
- `data/raw_manual/public_signal_layer_v2.csv` - public visibility coding file.
- `data/source_tracker/` - filing and borrower-row source tracking.
- `output/valuation_signal_summary.csv` - summary metrics.

The broader research motivation is to study how borrower-level credit deterioration becomes visible in opaque private debt markets.
