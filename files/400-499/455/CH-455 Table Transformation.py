import pandas as pd

path = "400-499/455/CH-455 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="B:G", skiprows=2, nrows=5)
test = pd.read_excel(path, usecols="I:L", skiprows=2, nrows=8)
test.columns = ["DATE", "CUSTOMER", "PRODUCT", "SALES"]

result = (
    input.rename(columns={"Date": "DATE", "Custoemr": "CUSTOMER"})
    .assign(_row=range(len(input)))
    .melt(["_row", "DATE", "CUSTOMER"], var_name="PRODUCT", value_name="SALES")
    .query("SALES != 0")
    .sort_values(["DATE", "CUSTOMER", "SALES"], ascending=[True, True, False])
    .drop(columns="_row")
    .reset_index(drop=True)
)
print(result.equals(test))
