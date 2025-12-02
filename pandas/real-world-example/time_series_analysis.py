import pandas as pd

# Create time series
dates = pd.date_range(start="2024-01-01", periods=7)
sales = [100, 120, 90, 150, 200, 180, 220]

df = pd.DataFrame({"date": dates, "sales": sales}).set_index("date")

print("Time Series:\n", df)

# Rolling average
print("\n7-Day Rolling Mean:\n", df.rolling(window=3).mean())
