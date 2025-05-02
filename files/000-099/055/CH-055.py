import pandas as pd
import numpy as np

input = pd.read_excel("CH-055 Warehouse Management.xlsx", usecols="B:E", skiprows=1)
test = pd.read_excel("CH-055 Warehouse Management.xlsx", usecols="H:K", skiprows=1, nrows= 3)

result = input.copy()
result["Year"] = result["Date"].dt.year
result = result.groupby(["Order No", "Product"]).agg({"Yea                                                                                              2r": "min","Quantity": "sum"}).reset_index()
result.drop(columns=["Order No"], inplace=True)
result = result.pivot_table(index="Product", columns="Year", values="Quantity", aggfunc="sum", fill_value=0).reset_index()

test.columns = result.columns
result.iloc[:, 1:] = result.iloc[:, 1:].astype(float)
result.iloc[:, 1:] = result.iloc[:, 1:].replace(0, np.NaN)

print(result.equals(test))  # True