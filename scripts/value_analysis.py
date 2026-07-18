import json
import pandas as pd

with open("data/raw/ipl_stats.json", "r", encoding="utf-8") as f:
    stats = json.load(f)

stats_df = pd.DataFrame(stats)
prices_df = pd.read_csv("data/raw/auction_prices.csv")

df = prices_df.merge(stats_df, on="name", how="inner")
print(f"Players with both price and stats: {len(df)}")

df["ipl_wkts"] = df["ipl_wkts"].fillna(0)
df["ipl_runs"] = df["ipl_runs"].fillna(0)

# Impact score: runs + (wickets x 20), a standard rough T20 equivalence used in cricket analytics
df["impact_score"] = df["ipl_runs"] + (df["ipl_wkts"] * 20)
df["value_per_crore"] = (df["impact_score"] / df["price_crore"]).round(1)

df = df.sort_values("value_per_crore", ascending=False)
df.to_csv("data/clean/player_value.csv", index=False)

print("\n=== FULL VALUE RANKING (impact points per crore spent) ===")
print(df[["name", "price_crore", "ipl_runs", "ipl_wkts", "impact_score", "value_per_crore"]].to_string(index=False))

print("\n=== BEST VALUE (top 5) ===")
print(df.head(5)[["name", "price_crore", "value_per_crore"]].to_string(index=False))

print("\n=== WORST VALUE / MOST OVERPAID (bottom 5) ===")
print(df.tail(5)[["name", "price_crore", "value_per_crore"]].to_string(index=False))