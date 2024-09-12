import pandas as pd

path = "CH-112 Custom Rank.xlsx"
input = pd.read_excel(path, usecols="C:E", skiprows=1)
input.columns = ["Product", "Y2022", "Y2023"]
test  = pd.read_excel(path, usecols="J:K", skiprows=1)
test.columns = ["Rank", "Product"]

result = input.copy()
result = input.assign(diff=input["Y2023"] - input["Y2022"])\
    .assign(Rank=lambda x: x["diff"]\
    .rank(ascending=False).astype(int))\
    .sort_values("Rank")[["Rank", "Product"]]\
    .reset_index(drop=True)

print(all(result == test)) # True