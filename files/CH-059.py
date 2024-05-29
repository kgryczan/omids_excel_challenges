import pandas as pd

input = pd.read_excel("CH-059 Merge Columns.xlsx", usecols="B:J", skiprows=1, nrows = 10)
test = pd.read_excel("CH-059 Merge Columns.xlsx", usecols="L:P", skiprows=1, nrows = 10)
test.columns = test.columns.str.replace(".1", "")

result = input.melt(id_vars=["Date"], var_name="time", value_name="value")
result["time"] = result["time"].str[:4] + "00"
result = result.pivot_table(index="Date", columns="time", values="value", aggfunc="sum").reset_index()

print(result.equals(test)) # True