import pandas as pd
import numpy as np
import re

path = "300-399/336/CH-336 Column Splitting .xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=6, dtype=str)
test = pd.read_excel(path, usecols="F:I", skiprows=1, nrows=6, dtype=str)

def insert_pipe(val):
    if pd.isna(val):
        return val
    return re.sub(r'(?<=\D)(?=\d)|(?<=\d)(?=\D)', '|', str(val))

input["ID"] = input["ID"].apply(insert_pipe)

split_cols = (
    input["ID"]
    .str.split("|", expand=True)
    .replace(["None", None], np.nan)
)
split_cols.columns = [f"ID {i+1}" for i in range(split_cols.shape[1])]

input = input.drop(columns=["ID"])

result = pd.concat([input, split_cols], axis=1)

print(result.equals(test)) # True
