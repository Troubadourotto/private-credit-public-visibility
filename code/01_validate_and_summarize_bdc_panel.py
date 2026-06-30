"""
Validate and summarize the BDC loan-mark pilot panel.

This script is intentionally simple. It is meant to demonstrate an RA-style
workflow: read a hand-collected borrower-level valuation panel, validate core
ratios and event flags, merge the public-visibility coding layer, and generate
summary tables/figures that can be audited and extended.

Run from the repository root:
    python code/01_validate_and_summarize_bdc_panel.py
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "processed" / "bdc_combined_valuation_panel_completed.csv"
SIGNAL_PATH = ROOT / "data" / "raw_manual" / "public_signal_layer_v2.csv"
TABLE_DIR = ROOT / "output" / "tables"
FIG_DIR = ROOT / "output" / "figures"
SUMMARY_PATH = ROOT / "output" / "valuation_signal_summary.csv"


MARKDOWN_THRESHOLDS = [-0.05, -0.075, -0.10]


def read_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    panel = pd.read_csv(DATA_PATH)
    signals = pd.read_csv(SIGNAL_PATH)
    return panel, signals


def validate_panel(panel: pd.DataFrame) -> pd.DataFrame:
    """Recalculate core variables and flag discrepancies."""
    df = panel.copy()

    df["calc_q4_fv_to_cost"] = df["q4_fair_value_mm"] / df["q4_cost_mm"]
    df["calc_q1_fv_to_cost"] = df["q1_fair_value_mm"] / df["q1_cost_mm"]
    df["calc_qoq_fv_to_cost_change"] = df["calc_q1_fv_to_cost"] - df["calc_q4_fv_to_cost"]
    df["calc_q4_level_markdown_event"] = (df["calc_q4_fv_to_cost"] < 0.90).astype(int)
    df["calc_q1_level_markdown_event"] = (df["calc_q1_fv_to_cost"] < 0.90).astype(int)
    df["calc_qoq_markdown_event"] = (df["calc_qoq_fv_to_cost_change"] < -0.05).astype(int)

    tolerance = 1e-6
    checks = {
        "q4_ratio_match": (df["q4_fv_to_cost"] - df["calc_q4_fv_to_cost"]).abs() < tolerance,
        "q1_ratio_match": (df["q1_fv_to_cost"] - df["calc_q1_fv_to_cost"]).abs() < tolerance,
        "qoq_change_match": (df["qoq_fv_to_cost_change"] - df["calc_qoq_fv_to_cost_change"]).abs() < tolerance,
        "q4_event_match": df["q4_markdown_event_level"] == df["calc_q4_level_markdown_event"],
        "q1_event_match": df["q1_markdown_event_level"] == df["calc_q1_level_markdown_event"],
        "qoq_event_match": df["qoq_markdown_event"] == df["calc_qoq_markdown_event"],
    }
    for col, values in checks.items():
        df[col] = values

    return df


def build_summary(panel: pd.DataFrame, signals: pd.DataFrame) -> pd.DataFrame:
    merged = panel[["Ticker", "borrower_clean_name", "qoq_markdown_event", "qoq_fv_to_cost_change"]].merge(
        signals[[
            "Ticker",
            "borrower_clean_name",
            "signal_found",
            "signal_strength",
            "pre_q1_observable",
            "signal_type",
        ]],
        on=["Ticker", "borrower_clean_name"],
        how="left",
        validate="one_to_one",
    )

    rows: list[dict[str, object]] = []
    rows.append({"metric": "Total observations", "value": len(panel)})
    rows.append({"metric": "Q4 level markdown events", "value": int(panel["q4_markdown_event_level"].sum())})
    rows.append({"metric": "Q1 level markdown events", "value": int(panel["q1_markdown_event_level"].sum())})

    for threshold in MARKDOWN_THRESHOLDS:
        count = int((panel["qoq_fv_to_cost_change"] < threshold).sum())
        rows.append({"metric": f"QoQ markdown events at {threshold:.1%} threshold", "value": count})

    near_cutoff = int((panel["qoq_fv_to_cost_change"].between(-0.06, -0.05, inclusive="both")).sum())
    rows.append({"metric": "Threshold-sensitive QoQ markdown cases within 1pp of -5pp cutoff", "value": near_cutoff})

    signal_found = signals["signal_found"].fillna("no").astype(str).str.lower().eq("yes")
    pre_q1 = signals["pre_q1_observable"].fillna("no").astype(str).str.lower().eq("yes")
    rows.append({"metric": "Public signal found, broad definition, any timing", "value": int(signal_found.sum())})
    rows.append({"metric": "Public signal found and observable by Q1 valuation date", "value": int((signal_found & pre_q1).sum())})
    rows.append({"metric": "No clear public signal found", "value": int((signals["signal_strength"] == 0).sum())})
    rows.append({"metric": "Borrower-specific hard credit/distress signals", "value": int((signals["signal_strength"] == 3).sum())})
    rows.append({"metric": "Borrower-specific soft signals", "value": int((signals["signal_strength"] == 2).sum())})
    rows.append({"metric": "Industry/comparable weak signals", "value": int((signals["signal_strength"] == 1).sum())})

    markdown = merged["qoq_markdown_event"] == 1
    pre_q1_signal = merged["pre_q1_observable"].fillna("no").astype(str).str.lower().eq("yes")
    rows.append({"metric": "QoQ markdown + hard borrower-specific signal", "value": int((markdown & (merged["signal_strength"] == 3)).sum())})
    rows.append({"metric": "QoQ markdown + soft borrower-specific signal", "value": int((markdown & (merged["signal_strength"] == 2)).sum())})
    rows.append({"metric": "QoQ markdown + pre-Q1 industry/comparable weak signal", "value": int((markdown & (merged["signal_strength"] == 1) & pre_q1_signal).sum())})
    rows.append({"metric": "QoQ markdown + no clear public signal", "value": int((markdown & (merged["signal_strength"] == 0)).sum())})

    return pd.DataFrame(rows)


def save_tables(panel: pd.DataFrame, signals: pd.DataFrame, summary: pd.DataFrame) -> None:
    TABLE_DIR.mkdir(parents=True, exist_ok=True)

    markdown_cases = panel.loc[panel["qoq_markdown_event"] == 1, [
        "BDC",
        "Ticker",
        "borrower_clean_name",
        "portfolio_company",
        "industry",
        "q4_fv_to_cost",
        "q1_fv_to_cost",
        "qoq_fv_to_cost_change",
        "q4_source_page",
        "q1_source_page",
        "sample_note",
    ]].merge(
        signals[[
            "Ticker",
            "borrower_clean_name",
            "signal_strength",
            "signal_type",
            "pre_q1_observable",
            "signal_summary",
            "deep_dive_conclusion",
        ]],
        on=["Ticker", "borrower_clean_name"],
        how="left",
    )

    signal_crosstab = pd.crosstab(
        signals["signal_strength"],
        signals["pre_q1_observable"].fillna("missing"),
        dropna=False,
    ).reset_index()

    panel[[
        "BDC",
        "Ticker",
        "borrower_clean_name",
        "industry",
        "q4_fv_to_cost",
        "q1_fv_to_cost",
        "qoq_fv_to_cost_change",
        "qoq_markdown_event",
    ]].to_csv(TABLE_DIR / "loan_level_panel_summary.csv", index=False)
    markdown_cases.to_csv(TABLE_DIR / "qoq_markdown_cases.csv", index=False)
    signal_crosstab.to_csv(TABLE_DIR / "public_signal_crosstab.csv", index=False)
    summary.to_csv(SUMMARY_PATH, index=False)


def make_figures(panel: pd.DataFrame, signals: pd.DataFrame) -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)

    # Figure 1: Q4 vs Q1 fair-value-to-cost ratios.
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(panel["q4_fv_to_cost"], panel["q1_fv_to_cost"])
    low = min(panel["q4_fv_to_cost"].min(), panel["q1_fv_to_cost"].min()) - 0.03
    high = max(panel["q4_fv_to_cost"].max(), panel["q1_fv_to_cost"].max()) + 0.03
    ax.plot([low, high], [low, high], linestyle="--", linewidth=1)
    ax.axhline(0.90, linestyle=":", linewidth=1)
    ax.axvline(0.90, linestyle=":", linewidth=1)
    ax.set_xlabel("Q4 fair value / cost")
    ax.set_ylabel("Q1 fair value / cost")
    ax.set_title("Q4 vs. Q1 BDC borrower-level valuation ratios")
    ax.set_xlim(low, high)
    ax.set_ylim(low, high)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "q4_q1_fv_cost_scatter.png", dpi=200)
    plt.close(fig)

    # Figure 2: visibility categories among QoQ markdown events.
    merged = panel[["Ticker", "borrower_clean_name", "qoq_markdown_event"]].merge(
        signals[["Ticker", "borrower_clean_name", "signal_strength"]],
        on=["Ticker", "borrower_clean_name"],
        how="left",
    )
    markdown_signals = merged.loc[merged["qoq_markdown_event"] == 1, "signal_strength"]
    labels = {
        0: "No clear\npublic signal",
        1: "Industry/comparable\nweak signal",
        2: "Borrower-specific\nsoft signal",
        3: "Borrower-specific\nhard signal",
    }
    counts = markdown_signals.value_counts().reindex([0, 1, 2, 3], fill_value=0)

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.bar([labels[i] for i in counts.index], counts.values)
    ax.set_ylabel("Number of QoQ markdown cases")
    ax.set_title("Public-visibility coding for QoQ markdown cases")
    ax.set_ylim(0, max(counts.max() + 1, 1))
    fig.tight_layout()
    fig.savefig(FIG_DIR / "qoq_markdown_signal_visibility.png", dpi=200)
    plt.close(fig)


def main() -> None:
    panel, signals = read_data()
    validated = validate_panel(panel)

    failed_checks = validated[[
        "q4_ratio_match",
        "q1_ratio_match",
        "qoq_change_match",
        "q4_event_match",
        "q1_event_match",
        "qoq_event_match",
    ]].eq(False).sum()

    if failed_checks.sum() > 0:
        print("Validation warnings:")
        print(failed_checks[failed_checks > 0])
    else:
        print("All core valuation/event checks passed.")

    summary = build_summary(panel, signals)
    save_tables(panel, signals, summary)
    make_figures(panel, signals)

    print(f"Wrote summary to: {SUMMARY_PATH.relative_to(ROOT)}")
    print(f"Wrote tables to: {TABLE_DIR.relative_to(ROOT)}")
    print(f"Wrote figures to: {FIG_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
