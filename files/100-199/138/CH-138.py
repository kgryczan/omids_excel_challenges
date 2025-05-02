import pandas as pd

path = "CH-138 Periodic Sales Summary.xlsx"
input = pd.read_excel(path, usecols="C:E", skiprows=1, nrows=26)
test = pd.read_excel(path, usecols="G:J", skiprows=1, nrows = 4 )

input['Month'] = input['Date'].dt.month
input['decade_days'] = 'P' + (((input['Date'].dt.day - 1) // 10 + 1).clip(upper=3)).astype(str)

result = input.pivot_table(index = "Month", columns = "decade_days", values = "Qty", aggfunc = "sum").reset_index()
result = result.fillna(0).astype("int64")
result.columns.name = None

print(test.equals(result)) # True