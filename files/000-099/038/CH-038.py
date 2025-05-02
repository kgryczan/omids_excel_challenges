import pandas as pd
from datetime import datetime, timedelta

input = pd.read_excel("CH-038 Duration Since Last Visit.xlsx", usecols="B:C", skiprows=1, nrows= 25)
test = pd.read_excel("CH-038 Duration Since Last Visit.xlsx", usecols="G:H", skiprows=1, nrows = 4)

dates = pd.date_range(start="2024-01-01", end="2024-05-01", freq="M").to_frame(name="end_of_month")

ends = pd.MultiIndex.from_product([dates["end_of_month"], input["Agent ID"].unique()], names=["Date", "Agent ID"]).to_frame(index=False)
ends["type"] = "end"

result = pd.concat([input.assign(type="visit"), ends]).sort_values(by=["Agent ID", "Date"])
result["last_visit"] = result["Date"].where(result["type"] == "visit").groupby(result["Agent ID"]).ffill()
result["month"] = result["Date"].dt.month.astype("int64")
result = result[result["type"] == "end"]
result["datediff"] = (result["Date"] - result["last_visit"]).dt.days
result = result.groupby("month")["datediff"].mean().reset_index()

result.columns = ["Month", "AVG Duration from Last Visit"]
print(result.equals(test)) # True