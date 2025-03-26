import pandas as pd

path = "CH-209 Combining the columns.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="E", skiprows=1, nrows=6).rename(columns=lambda col: col.split(".")[0] if "." in col else col)

input["Text"] = input["Text"].apply(lambda x: ''.join(w[0] for w in x.split()))
print(input.equals(test)) #True
