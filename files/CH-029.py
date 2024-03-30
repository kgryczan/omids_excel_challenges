import pandas as pd

input = pd.read_excel("CH-029 Identifying Customers Staple Products.xlsx", sheet_name="Sheet1", usecols="B:E", skiprows=1)
test = pd.read_excel("CH-029 Identifying Customers Staple Products.xlsx", sheet_name="Sheet1", usecols="I:J", skiprows=1, nrows = 4)

result = input.groupby(["Customer ID", "Product"]).agg(total_quantity=("Quantity", "sum")).reset_index()
result["rank"] = result.groupby("Customer ID")["total_quantity"].rank(ascending=False)
result["lowest_rank"] = result.groupby("Customer ID")["rank"].transform("min")
result = result[result["rank"] == result["lowest_rank"]]
result = result.groupby("Customer ID").agg({"Product": lambda x: ",".join(sorted(x))}).reset_index()
result = result.rename(columns={"Product": "Most Purchased PRODUCT"})

print(result["Most Purchased PRODUCT"].equals(test["Most Purchased PRODUCT"])) # True