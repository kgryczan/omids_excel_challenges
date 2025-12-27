import numpy as np
import pandas as pd
import re

path = "300-399/347/CH-347 Column Splitting.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=2, nrows=6)
test = pd.read_excel(path, usecols="F:I", skiprows=2, nrows=6)
test = test.fillna("")
for col in test.columns:
    test[col] = test[col].apply(lambda x: str(int(x)) if isinstance(x, float) and x.is_integer() else str(x))

def add_pipe(s):
    return re.sub(r"(?<=\D{2})(?=\d{2})|(?<=\d{2})(?=\D{2})", "|", str(s))
input['ID'] = input['ID'].astype(str).apply(add_pipe)
split_cols = input['ID'].str.split('|', expand=True)

for i, col in enumerate(split_cols.columns):
    input[f'ID {i+1}'] = split_cols[col].astype(str)

result = input[[f'ID {i+1}' for i in range(split_cols.shape[1])]]
result = result.replace({'None': ''}).astype(str)

print(result.equals(test))
# True