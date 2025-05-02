import pandas as pd

path = "CH-155 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="C:E", skiprows=1, nrows=21)
test = pd.read_excel(path, usecols="G:I", skiprows=1, nrows=10)
test.columns = input.columns

input.columns = ["Date", "Description", "Qty"]
input["Date"] = input["Date"].ffill()
input["Description"] = input["Description"].shift(-1)
input["Qty"] = input["Qty"].shift(-2)
input.loc[(input["Description"].notna()) & (input["Qty"].isna()), "Qty"] = "-"
input.dropna(inplace=True)
input["Date"] = pd.to_datetime(input["Date"]).dt.strftime('%d-%m-%Y')
input.reset_index(drop=True, inplace=True)

# had the same values, but cannot convert to common format. :D
print(input)
