import pandas as pd

path = "300-399/392/CH-392 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="B:C", nrows=25, skiprows=2)
test = pd.read_excel(path, usecols="E:H", nrows=6, skiprows=2)

input["group"] = (input["Col1"] == "Date").cumsum()
result = input.pivot(index="group", columns="Col1", values="Col 2").reset_index(drop=True)
result = result[["Date", "Customer", "Product", "Sale"]]

print((result == test).all().all())
# Output: True