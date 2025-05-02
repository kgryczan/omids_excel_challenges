import pandas as pd

path = "CH-094 Two Column Text.xlsx"
input = pd.read_excel(path, skiprows=1, usecols = "B:C")
test  = pd.read_excel(path, skiprows=1, usecols = "H:J", nrows = 7)
test.columns = test.columns.str.replace(".1", "")

result = input.copy()
result["RowNumber"] = result.groupby("Group").cumcount() + 1
result["col"] = result["RowNumber"].apply(lambda x: 2 if x % 2 == 0 else 1)
result["row"] = result["RowNumber"].apply(lambda x: (x + 1) // 2)

result = result.pivot(index = ["Group", "row"], columns = "col", values = "Text")
result.columns = [f"Column {col}" for col in result.columns]
result = result.reset_index()
result = result.drop(columns = "row")

print(result.equals(test)) # True