import pandas as pd
import numpy as np

path = "400-499/411/CH-411 Column Splitting.xlsx"
input = pd.read_excel(path, usecols="B", nrows=7, skiprows=2)
test = pd.read_excel(path, usecols="F:H", nrows=7, skiprows=2).replace(np.nan, "")

def split_mod(x, n=3):
	if pd.isna(x):
		return [pd.NA] * n
	chars = list(str(x))
	parts = [pd.to_numeric("".join(chars[i - 1 :: n]), errors="ignore") for i in range(1, n + 1)]
	return parts
parts = input["ID"].map(split_mod)
parts_df = pd.DataFrame(parts.tolist(), columns=["ID1", "ID2", "ID3"])
result = (
	pd.concat([input.drop(columns=["ID"]), parts_df], axis=1)
    .replace(np.nan, "")
)

print(result.equals(test))
# True