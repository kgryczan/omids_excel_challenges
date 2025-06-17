import pandas as pd
import re

path = "200-299/249/CH-249 Extract from Text.xlsx"

input = pd.read_excel(path, usecols="B", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="D", skiprows=1, nrows=4)
pattern = r"[A-Z]{1}[a-z]{1}[0-9]{1}-[0-9]{2}"
result = input.iloc[:, 0].astype(str).str.extract(f'({pattern})').dropna().reset_index(drop=True).rename(columns={0: 'Product ID'})

print(result.equals(test))
