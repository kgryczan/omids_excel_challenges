import pandas as pd

path = "400-499/425/CH-425 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="B:E", nrows=3, skiprows=2)
test = pd.read_excel(path, usecols="G:J", nrows=9, skiprows=2)

result = input.melt(
    id_vars=input.columns[0], var_name="CUSTOMER", value_name="VALUE"
).dropna()
result["VALUE"] = result["VALUE"].str.split(",")
result = result.explode("VALUE").reset_index(drop=True)
result[["PRODUCT", "SALES"]] = result["VALUE"].str.split(":", n=1, expand=True)
result["SALES"] = pd.to_numeric(result["SALES"])
result = result.rename(columns={result.columns[0]: "DATE"}).drop(columns="VALUE")
result = result.sort_values("DATE").reset_index(drop=True)

print(result.equals(test))
# True
