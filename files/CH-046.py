import pandas as pd

input = pd.read_excel("CH-046 Numbers Cleaning.xlsx",  usecols="B", skiprows=1, nrows=15)
test = pd.read_excel("CH-046 Numbers Cleaning.xlsx",  usecols="J", skiprows=1, nrows=5)
test.columns = ["Product ID"]

result = input.sort_values("Product ID").reset_index(drop=True) 
result["lag"] = result["Product ID"].shift(1)
result["diff"] = result["Product ID"] - result["lag"]
result["diff"] = result["diff"].fillna(1.0)
result["cumsum"] = result["diff"].gt(1).cumsum()

result2 = result.groupby("cumsum").agg({"Product ID": ["max", "min"]}) 
result2.columns = result2.columns.droplevel(0)
result2["Product ID"] = result2.apply(lambda x: x["min"] if x["min"] == x["max"] else str(x["min"]) + "-" + str(x["max"])[2:4], axis=1)
result2 = result2.drop(columns=["max", "min"]).reset_index(drop=True)

print(result2.equals(test)) # True