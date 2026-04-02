import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
df = pd.read_csv("data/processed/master.csv", parse_dates=["date"])
df = df.set_index("date").sort_index()
cutoff = df.index.max() - pd.DateOffset(years=2)
df = df[df.index >= cutoff].copy()
print("Window:", df.index.min().date(), "to", df.index.max().date())
def scale(s): return (s - s.min()) / (s.max() - s.min()) * 100
df["chile_scaled"] = scale(df["chile_copper_production_mt"])
df["usdcny_inv"] = 100 - scale(df["usdcny_close"])
df["composite"] = 0.625 * df["chile_scaled"] + 0.375 * df["usdcny_inv"]
df["signal"] = np.where(df["composite"] >= 60, 1, np.where(df["composite"] <= 40, -1, 0))
df["fwd_return"] = df["lme_close"].pct_change(21).shift(-21)
bull = df[df["signal"] == 1].dropna(subset=["fwd_return"])
bear = df[df["signal"] == -1].dropna(subset=["fwd_return"])
all_sig = df[df["signal"] != 0].dropna(subset=["fwd_return"])
bull_hr = (bull["fwd_return"] > 0).mean() * 100
bear_hr = (bear["fwd_return"] < 0).mean() * 100
overall = ((bull["fwd_return"] > 0).sum() + (bear["fwd_return"] < 0).sum()) / len(all_sig) * 100
print("Bullish:", len(bull), "Hit rate:", round(bull_hr,1), "%")
print("Bearish:", len(bear), "Hit rate:", round(bear_hr,1), "%")
print("OVERALL HIT RATE:", round(overall,1), "%")
