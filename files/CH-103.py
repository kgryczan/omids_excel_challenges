import pandas as pd
import numpy as np

path = "CH-103 Custom Average.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows = 1, nrows = 19)
test = pd.read_excel(path, usecols="I:J", skiprows = 1, nrows = 4)

today = pd.to_datetime("2024-08-20")

input["Delivery Time"] = (input["Delivery Date"] - input["Order Date"]).dt.days
input["Adjusted Delivery Time"] = np.where(input["Delivery Date"].isnull(), (today - input["Order Date"]).dt.days, input["Delivery Time"])
input = input[input["Delivery Time"].notnull() | (input["Adjusted Delivery Time"] > input.groupby("Product ID")["Delivery Time"].transform("mean"))]\
    .groupby("Product ID")["Adjusted Delivery Time"].mean().reset_index()

print(input["Adjusted Delivery Time"].equals(test["Avg delivery time"])) # True