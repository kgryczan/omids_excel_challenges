import pandas as pd

path = "400-499/445/CH-445 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="B:F", nrows=9, skiprows=2)
test = pd.read_excel(path, usecols="H:K", nrows=9, skiprows=2)
test.columns = ["DATE", "CUSTOMER", "PRODUCT", "SALES"]

result = (
    input.melt(
        id_vars=["DATE", "PRODUCT"],
        value_vars=["C1", "C2", "C3"],
        var_name="CUSTOMER",
        value_name="SALES",
    )
    .dropna(subset=["SALES"])
    .sort_values(["DATE", "CUSTOMER"], kind="stable")
    [["DATE", "CUSTOMER", "PRODUCT", "SALES"]]
    .reset_index(drop=True)
)
result["SALES"] = result["SALES"].astype(test["SALES"].dtype)

print(result.equals(test))
