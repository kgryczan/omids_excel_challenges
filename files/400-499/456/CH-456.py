import pandas as pd

path = "400-499/456/CH-456 Number Series.xlsx"
input = pd.read_excel(path, usecols="B:C", nrows=3, skiprows=2)
test = pd.read_excel(path, usecols="E:F", nrows=8, skiprows=2)
test.columns = ["Date", "Sale"]

result = (
    input.set_index("Date")
    .reindex(pd.date_range(input["Date"].min(), input["Date"].max()))
    .interpolate()
    .astype({"Sale": int})
    .rename_axis("Date")
    .reset_index()
)

print(result.equals(test))
