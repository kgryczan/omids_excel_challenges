import pandas as pd

input_data = pd.read_excel("CH-021 Transformation.xlsx", usecols="B:E", skiprows=1, nrows=10)
test = pd.read_excel("CH-021 Transformation.xlsx", usecols="G:H", skiprows=1, nrows=7)

result = (
    input_data.rename(columns={input_data.columns[1]: "Product_1", input_data.columns[2]: "Product_2", input_data.columns[3]: "Product_3"})
    .melt(id_vars="Machinary code", var_name="Product", value_name="Value")
    .dropna(subset=["Value"])
    .sort_values("Product")
    .groupby("Value", as_index=False)["Machinary code"]
    .agg(lambda s: " ,".join(s.astype(str)))
    .rename(columns={"Value": "Product Code", "Machinary code": "Machinary Code"})
)

print(result.equals(test))
