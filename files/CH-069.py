import pandas as pd
import numpy as np

path = "CH-069 Sales by State.xlsx"

input1 = pd.read_excel(path, usecols="B:D", skiprows=1)
input2 = pd.read_excel(path, usecols="F:H", skiprows=1, nrows = 11)
input2.columns = input2.columns.str.replace(".1", "")
test = pd.read_excel(path, usecols="J:K", skiprows=1, nrows = 5)
test.columns = test.columns.str.replace(".1", "")

input2 = input2.sort_values(by="Customer ID").reset_index(drop=True)
input2["end_date"] = input2.groupby("Customer ID")["Date"].shift(-1)
input2["end_date"].fillna(pd.Timestamp.today().date(), inplace=True)
input2["end_date"] = pd.to_datetime(input2["end_date"])

res = input1.merge(input2, how="left", on="Customer ID")
res = res[(res["Date_x"] <= res["end_date"]) & (res["Date_x"] >= res["Date_y"])]
res = res.groupby("States").agg({"Quantity": "sum"}).rename(columns={"Quantity": "Sales"}).reset_index()

print(res)