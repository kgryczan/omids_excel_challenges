import pandas as pd

input = pd.read_excel("CH-036 Pareto Line.xlsx", usecols="B:E", nrows = 14, skiprows=1)
test = pd.read_excel("CH-036 Pareto Line.xlsx", usecols="H", nrows=7).dropna().astype(int).reset_index(drop=True)
result = input.assign(row_id=range(1, len(input) + 1)).apply(lambda row: not any((input.iloc[:, 1:4] > row[1:4]).all(axis=1)), axis=1)
result = result[result].index.to_frame(index=False).rename(columns={0: "Result"}) + 1
result["Result"] = result["Result"].astype(int)

print(result.equals(test)) # True
