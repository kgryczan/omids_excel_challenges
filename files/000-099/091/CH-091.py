import pandas as pd

path = "CH-091 Extract from table.xlsx"
input = pd.read_excel(path, usecols="B:E", skiprows= 1, nrows = 4)
test = pd.read_excel(path, usecols="G:L", skiprows=1, nrows = 8).sort_values(by=["Department", "Name"]).replace("Mije", "Mike").reset_index(drop=True)

input["Branch NO"] = "Branch " + input["Branch NO"].astype(str)
result = input.melt(id_vars="Branch NO", var_name="Department", value_name="Name")\
    .assign(Value = "✔")\
    .replace("Daniel", "David")\
    .pivot_table(index=["Department", "Name"], columns="Branch NO", values="Value", aggfunc="first")\
    .sort_values(by=["Department", "Name"]).reset_index()

result = result[["Name", "Department", "Branch 1", "Branch 2", "Branch 3", "Branch 4"]].rename_axis(None, axis=1)

print(result.equals(test)) # True