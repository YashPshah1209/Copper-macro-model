# Copper Macro Model
### Quantitative LME Copper Price Direction Forecasting

A macro-driven quantitative model that forecasts LME copper price direction 
using two statistically significant variables: Chilean copper production and 
the USD/CNY exchange rate.

---

## Key Results
| Metric | Value |
|--------|-------|
| R² (Model Fit) | 0.955 |
| Bullish Signal Hit Rate | 72.7% |
| Overall Hit Rate | 55.8% |
| Avg Return on Bullish Signal | +9.3% (3-month forward) |
| Backtest Period | Jan 2020 – Apr 2026 (76 months) |

---

## Model Variables
| Variable | Weight | Direction | p-value |
|----------|--------|-----------|---------|
| Chile Copper Production | 62.5% | Inverted (low supply = bullish) | 0.023 |
| USD/CNY Exchange Rate | 37.5% | Inverted (weak USD = bullish) | 0.041 |
| COMEX Volume | Dropped | — | 0.166 (not significant) |

---

## Composite Score Formula
```
Composite = 0.625 × (100 - Chile_scaled) + 0.375 × (100 - USDCNY_scaled)
```
- Score ≥ 70th percentile → **Bullish signal**
- Score ≤ 30th percentile → **Bearish signal**

---

## Project Structure
```
copper-macro-model/
├── data/
│   ├── raw/          # Chile production, USD/CNY, LME price CSVs
│   └── processed/    # master.csv (merged dataset)
├── scripts/          # Python analysis scripts
├── charts/           # 6 generated visualisation charts
└── README.md
```

---

## Methodology
- **Regression:** OLS with 74 observations, F-stat 495.1 (p < 4.84e-47)
- **Backtest:** 3-month forward returns, percentile-based signal thresholds
- **Signal logic:** Percentile thresholds (70th/30th) to handle skewed score distribution

---

## Limitations
- Bullish signals concentrated in 2020–2022 supercycle — cross-cycle validation needed
- High R² may partly reflect co-trending variables (spurious regression risk)
- 76 months of data — extending to 2015 would strengthen robustness

---

## Tools Used
Python 3.14 | pandas | numpy | statsmodels | matplotlib | OLS Regression
