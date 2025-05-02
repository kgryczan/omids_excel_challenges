import pandas as pd

path = "CH-224 Column Splitting.xlsx"

input = pd.read_excel(path, usecols="B", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="D:E", skiprows=1, nrows=6)

result = input["ID"].str.split("-", expand=True)
result.columns = ["ID1", "ID2", "ID3", "ID4", "ID5"]

result["ID.1"] = result[["ID1", "ID2"]].apply(lambda x: "-".join(x.dropna()), axis=1)
result["ID.2"] = result[["ID3", "ID4", "ID5"]].apply(lambda x: "-".join(x.dropna()), axis=1)

result = result[["ID.1", "ID.2"]]

print(result.equals(test)) # True