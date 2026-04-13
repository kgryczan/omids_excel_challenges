import pandas as pd

path = "300-399/396/CH-396 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="B", nrows=2, skiprows=1)
test = pd.read_excel(path, usecols="C:F", nrows=7, skiprows=5)

result = (
    input["Question"]
    .str.split("\n").explode()
    .str.split("\t", expand=True)
)
result.columns = result.iloc[0]
result = result.iloc[1:].assign(Sale=lambda df: df["Sale"].astype(int)).reset_index(drop=True)

print(result.equals(test))
# True