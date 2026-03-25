import pandas as pd

input_data = pd.read_excel("CH-018 Sales Calendar Extraction.xlsx", usecols="B:C", skiprows=1, nrows=120)
test_month = 2
test = pd.read_excel("CH-018 Sales Calendar Extraction.xlsx", usecols="I:O", skiprows=1, nrows=6)

input_data["Date"] = pd.to_datetime(input_data["Date"])
all_dates = pd.DataFrame({"Date": pd.date_range(input_data["Date"].min(), input_data["Date"].max(), freq="D")})
result = all_dates.merge(input_data, on="Date", how="left")
result["month"] = result["Date"].dt.month
result["wday"] = result["Date"].dt.day_name().str[:3]
result["week"] = result["Date"].dt.isocalendar().week.astype(int)
monthly_avg = result.groupby("month")["Quantity"].transform(lambda s: round(s.dropna().mean(), 0))
result["monthly_av"] = monthly_avg
result = result.loc[result["month"] == test_month].copy()
result["Quantity_check"] = result.apply(
    lambda r: "L" if pd.notna(r["Quantity"]) and r["Quantity"] <= r["monthly_av"]
    else ("U" if pd.notna(r["Quantity"]) and r["Quantity"] > r["monthly_av"] else "-"),
    axis=1,
)
result = result[["wday", "week", "Quantity_check"]].pivot(index="week", columns="wday", values="Quantity_check").reset_index(drop=True)
result = result.rename(columns={"Sun": "Su", "Mon": "Mo", "Tue": "Tu", "Wed": "We", "Thu": "Th", "Fri": "Fr", "Sat": "Sa"})
result = result[["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]]

print(result.equals(test))
