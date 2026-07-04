import pandas as pd

path = "400-499/437/CH-437 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:D", nrows=12, skiprows=2)
test = pd.read_excel(path, usecols="F:G", nrows=5, skiprows=2)

input["sorted_products"] = (
    input["Products"]
    .str.split(",")
    .apply(lambda x: ",".join(sorted(p.strip() for p in x)))
)
aggregated = (
    input.groupby("sorted_products", as_index=False, sort=False)["Quantity"]
    .sum()
    .rename(columns={"Quantity": "Quantity_sum"})
)
aggregated.columns = test.columns
print(aggregated.equals(test))
# BMD should be BDM
