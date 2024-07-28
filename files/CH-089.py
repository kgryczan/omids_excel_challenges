import pandas as pd

path = "CH-089 Transformation.xlsx"
input = pd.read_excel(path, usecols="B:G", skiprows=1, nrows=9, header=None)
test = pd.read_excel(path, usecols="I:K", skiprows=1)

input.iloc[0] = input.iloc[0].ffill()
input.columns = input.iloc[1] + " " + input.iloc[0]
input = input.drop([0, 1]).reset_index(drop=True)

input = input.stack().reset_index()
input[["Measure", "Product"]] = input["level_1"].str.split(" ", expand=True)
input = input.rename(columns={0: "Value"}).drop(["level_1", "level_0"], axis=1)

input["rowname"] = input.index // 2
input = input.pivot(index=["rowname", "Product"], columns="Measure", values="Value")\
    .sort_values(["Product", "Date"]).reset_index()
input.columns.name = None
input["Date"] = pd.to_datetime(input["Date"])
input["Quantity"] = input["Quantity"].astype("int64")
input = input[["Date", "Product", "Quantity"]]

print(input.equals(test))  # True
