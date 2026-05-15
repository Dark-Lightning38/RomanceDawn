# generate_pnl_data.py — run this ONCE to create your practice data

import pandas as pd
import numpy as np
import random

random.seed(42)
np.random.seed(42)

# ── LINE ITEMS ─────────────────────────────────────────
LINES = [
    # (line_item, section, is_ratio, sort_order, is_subtotal)
    ("GWP",                                          "Technical", False, 1,  False),
    ("GWP Net of IC and FREASS",                     "Technical", False, 2,  False),
    ("GEP",                                          "Technical", False, 3,  False),
    ("Claims CY net",                                "Technical", False, 4,  False),
    ("o/w Claims CY",                                "Technical", False, 5,  False),
    ("o/w Reins. result CY",                         "Technical", False, 6,  False),
    ("Commissions",                                  "Technical", False, 7,  False),
    ("Technical result CY",                          "Technical", False, 8,  True),
    ("PY impact on claims",                          "Technical", False, 9,  False),
    ("Technical Result AY",                          "Technical", False, 10, True),
    ("Claims Handling costs",                        "Overheads", False, 11, False),
    ("o/w Labour cost",                              "Overheads", False, 12, False),  # sub-line
    ("Non-Commission expenses",                      "Overheads", False, 13, False),
    ("Acquisition costs",                            "Overheads", False, 14, False),
    ("Administrative costs",                         "Overheads", False, 15, False),
    ("Total Overheads excl MFR ITR TPA",             "Overheads", False, 16, True),
    ("Operating result excl ITR/MFR",                "Operating", False, 17, True),
    ("IT rebilling",                                 "Operating", False, 18, False),
    ("Management fees rebilling",                    "Operating", False, 19, False),
    ("Central costs not recharged (CCNR)",           "Operating", False, 20, False),
    ("Operating result Full loaded",                 "Operating", False, 21, True),
    ("Total Financial result",                       "Financial", False, 22, False),
    ("Tax on Underlying Earnings",                   "Financial", False, 23, False),
    ("Underlying Earnings fully loaded",             "Financial", False, 24, True),
    ("Transfer Pricing Flow",                        "Financial", False, 25, False),
    ("Underlying Earnings excl CCNR",                "Financial", False, 26, True),
    ("Loss ratio CY",                                "Ratios",    True,  27, False),
    ("Loss ratio PY",                                "Ratios",    True,  28, False),
    ("Commission ratio",                             "Ratios",    True,  29, False),
    ("CHC ratio",                                    "Ratios",    True,  30, False),
    ("NCE ratio",                                    "Ratios",    True,  31, False),
    ("CoR CY",                                       "Ratios",    True,  32, True),
    ("CoR AY",                                       "Ratios",    True,  33, True),
    ("Full loaded COR CY",                           "Ratios",    True,  34, True),
    ("Total ECR",                                    "Ratios",    True,  35, True),
]

VERSIONS  = ["Budget", "Forecast1", "Forecast2", "Actuals"]
PERIODS   = ["Jan", "Feb", "Mar", "Q1", "Apr", "May", "Jun",
             "Q2", "H1", "Q3", "Q4", "2026FY"]
LOBS      = ["Motor", "Travel", "Home", "CHC"]

# ── BASE VALUES PER LINE (realistic anchors) ────────────
BASE = {
    "GWP": 155.0, "GWP Net of IC and FREASS": 55.0, "GEP": 150.0,
    "Claims CY net": -35.0, "o/w Claims CY": -34.5, "o/w Reins. result CY": -0.3,
    "Commissions": -63.0, "Technical result CY": 55.0, "PY impact on claims": 0.5,
    "Technical Result AY": 55.5, "Claims Handling costs": -20.0, "o/w Labour cost": -8.0,
    "Non-Commission expenses": -12.0, "Acquisition costs": -5.5,
    "Administrative costs": -7.0, "Total Overheads excl MFR ITR TPA": -38.0,
    "Operating result excl ITR/MFR": 25.0, "IT rebilling": -2.5,
    "Management fees rebilling": -2.5, "Central costs not recharged (CCNR)": -4.0,
    "Operating result Full loaded": 16.0, "Total Financial result": 2.2,
    "Tax on Underlying Earnings": -6.0, "Underlying Earnings fully loaded": 12.5,
    "Transfer Pricing Flow": 0.0, "Underlying Earnings excl CCNR": 17.0,
    "Loss ratio CY": 23.0, "Loss ratio PY": 22.0, "Commission ratio": 40.0,
    "CHC ratio": 13.0, "NCE ratio": 8.0, "CoR CY": 83.0, "CoR AY": 83.0,
    "Full loaded COR CY": 90.0, "Total ECR": 95.0, }

LOB_SCALE = {"Motor": 1.0, "Travel": 0.35, "Home": 0.25, "CHC": 0.18}

VERSION_DRIFT = {"Budget": 0.0, "Forecast1": 0.03, "Forecast2": 0.05, "Actuals": 0.07}

PERIOD_SCALE  = {
    "Jan":0.08,"Feb":0.08,"Mar":0.09,"Q1":0.25,
    "Apr":0.08,"May":0.08,"Jun":0.09,"Q2":0.25,
    "H1":0.50,"Q3":0.25,"Q4":0.25,"2026FY":1.0
}

rows = []
for line, section, is_ratio, sort_order, is_subtotal in LINES:
    base = BASE.get(line, 0.0)
    for version in VERSIONS:
        for period in PERIODS:
            for lob in LOBS:
                drift  = np.random.normal(VERSION_DRIFT[version], 0.02)
                scale  = LOB_SCALE[lob] * PERIOD_SCALE[period]
                if is_ratio:
                    val = round(base * (1 + drift) + np.random.normal(0, 0.5), 1)
                else:
                    val = round(base * scale * (1 + drift), 2)
                rows.append({
                    "line_item":    line,
                    "section":      section,
                    "is_ratio":     is_ratio,
                    "sort_order":   sort_order,
                    "is_subtotal":  is_subtotal,
                    "version":      version,
                    "period":       period,
                    "lob":          lob,
                    "value":        val,
                })

df = pd.DataFrame(rows)
df.to_csv("axa_pnl_long.csv", index=False)
print(f"Done — {len(df)} rows written to axa_pnl_long.csv")
print(df.head(10))