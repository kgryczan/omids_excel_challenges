import pandas as pd

input_data = pd.read_excel("CH-011.xlsx", usecols="B:E", skiprows=1, nrows=15)
test = pd.read_excel("CH-011.xlsx", usecols="K", skiprows=1, nrows=5)

result = (
    input_data.melt(var_name="columns", value_name="codes")
    .groupby("codes", as_index=False)["columns"]
    .nunique()
    .rename(columns={"columns": "is_in_col"})
)
result = result.loc[result["is_in_col"] >= 3, ["codes"]]

print(result["codes"].equals(test["Item Code"]))
