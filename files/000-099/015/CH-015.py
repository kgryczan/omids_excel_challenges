import pandas as pd

input_data = pd.read_excel("CH-015.xlsx", usecols="B:E", skiprows=1, nrows=11)
test = pd.read_excel("CH-015.xlsx", usecols="G:S", skiprows=1, nrows=5)

input_data["nr"] = input_data.groupby("Product Code").cumcount() + 1
result = input_data.pivot(index="Product Code", columns="nr", values=["Ship Date", "Po number", "Po Quantity"])
result.columns = [f"{a} {b}" for a, b in result.columns]
keep = [c for c in result.columns if c.endswith("1") or c.endswith("2") or c.endswith("3") or c.endswith("4")]
result = result.reset_index()[["Product Code"] + keep].rename(columns={"Product Code": "Products"})

print(result.equals(test))
