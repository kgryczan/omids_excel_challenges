import pandas as pd

path = "200-299/272/CH-272 Find Value.xlsx"
df = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=7)
test = sorted(pd.read_excel(path, usecols="F", skiprows=1, nrows=12).iloc[:, 0].tolist())

unique = sorted(
    v for c in df for i, v in df[c].items()
    if (df[c] == v).sum() == 1 and (df.loc[i] == v).sum() == 1
)

print(unique == test)  # True