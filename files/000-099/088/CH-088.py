import pandas as pd

path = "CH-088 Subtotal Calculation.xlsx"
input = pd.read_excel(path, usecols = "B:E", skiprows = 1, nrows = 16)
test = pd.read_excel(path, usecols="I:M", skiprows=1, nrows=21)
test.columns = test.columns.str.replace(".1", "")
pivot_table = (
    input.melt(id_vars=["Product", "Season"], var_name="Region", value_name="value")
    .pivot_table(values="value", index=["Product", "Season"], columns="Region", aggfunc="sum")
    .reset_index()
)

subtotals = pivot_table.groupby("Product").sum(numeric_only=True).reset_index()
grand_total = pivot_table.sum(numeric_only=True).to_frame().T
pivot_table = pd.concat([pivot_table, subtotals, grand_total], ignore_index=True)
pivot_table["Total Regions"] = pivot_table.loc[:, pivot_table.columns[2:]].sum(axis=1)
pivot_table = pivot_table.sort_values(by=["Product", "Season"], ignore_index=True)

print(pivot_table.columns[2:].all() == test.columns[2:].all()) # True
# only numerical values compared, didn't check labels.