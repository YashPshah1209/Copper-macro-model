# Copper Macro Model
### Quantitative LME Copper Price Direction Forecasting

A macro-driven quantitative model that forecasts LME copper price direction
using two statistically significant variables: Chilean copper production and
the USD/CNY exchange rate. Built across two phases: OLS regression modelling
and full EDA + backtest implementation.

---

## Key Results
| Metric | Value |
|--------|-------|
| R² (Model Fit) | 0.940 |
| Adj R² | 0.948 |
| MAE (% of avg price) | 3.4% |
| Hit Rate when Long Signal | 63.2% |
| Avg Return when Signal On | +1.33% / month |
| Avg Return when Signal Off | +1.18% / month |
| Backtest Period | Jan 2020 – Apr 2026 (76 months) |
| Current Signal (Apr 2026) | 1 / 3 — BEARISH |

---

## Model Variables
| Variable | Direction | p-value |
|----------|-----------|---------|
| Chile Copper Production | Positive (co-trend with price) | 0.000 |
| USD/CNY Exchange Rate | Positive (weaker yuan = lower price) | 0.022 |
| COMEX Volume | Dropped — not significant | 0.166 |

---

## Composite Signal Score (0–3)
Each month scores 1 point per bullish condition met:

| Signal | Condition |
|--------|-----------|
| USD/CNY | Falling MoM (yuan strengthening) |
| Chile Production | Falling MoM (supply squeeze) |
| Price Momentum | LME close above 3-month rolling avg |

- Score ≥ 2 → **Bullish** (go long next month)
- Score ≤ 1 → **Bearish** (stay out)

### Score Distribution (76 months)
| Score | Months | Label |
|-------|--------|-------|
| 0 | 5 | Full Bear |
| 1 | 13 | Bear |
| 2 | 34 | Mild Bull |
| 3 | 4 | Full Bull |

---

## Backtest Summary
- Strategy (signal ≥ 2): **$1.540** final value
- Buy & Hold copper: **$2.202** final value
- The signal shows genuine 63.2% directional accuracy
- Better suited as a **risk overlay** than standalone long/short strategy
- In a strong bull trend, staying out of bearish months sacrifices upside
  but significantly reduces drawdowns

---

## Project Structure
```
copper-macro-model/
├── data/
│   ├── raw/                          # Chile production, USD/CNY, LME CSVs
│   └── processed/master.csv          # Merged dataset
├── notebooks/
│   ├── 01_exploration.ipynb          # Task 1 — initial exploration
│   └── Copper_macro_model.ipynb      # Task 2 — full EDA, OLS, backtest
├── charts/
│   ├── lme_price_history.png
│   ├── usdcny_chile_production.png
│   ├── correlation_matrix.png
│   ├── fitted_vs_actual.png
│   ├── composite_score.png
│   └── equity_curve.png
├── scripts/
├── copper_model_final.csv            # Enriched dataset (23 columns, 76 rows)
├── model_summary.txt                 # Backtest summary
└── README.md
```

---

## Methodology
- **Regression:** OLS with StandardScaler normalisation, 76 observations
- **Variables:** Chile copper production (MT) + USD/CNY exchange rate
- **Signal:** 3-component composite score, monthly frequency
- **Backtest:** Next-month forward returns, long-only when score ≥ 2

---

## Limitations
- High R² partly reflects co-trending variables (spurious regression risk)
- Chile production coefficient is positive due to shared upward trend —
  not a pure supply signal
- 76 months of data — extending to 2015 would improve robustness
- Signal performs better as risk filter than return maximiser in bull markets

---

## Tools Used
Python 3.14 | pandas | numpy | statsmodels | scikit-learn | matplotlib | seaborn
