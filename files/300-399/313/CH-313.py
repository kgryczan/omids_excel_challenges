import pandas as pd
from pprint import pprint

path = "300-399/313/CH-313 Table Transformation.xlsx"

input = pd.read_excel(path, usecols="B:J", skiprows=1, nrows=7)
test  = pd.read_excel(path, usecols="L:O", skiprows=1, nrows=5).astype(str)

output = []
for i, row in input.iterrows():
    first_valid_index = row.first_valid_index()
    last_index = row.last_valid_index()
    if first_valid_index is not None and last_index is not None:
        new_row = row.loc[first_valid_index:last_index]
        new_row.index = [f"Column{j+1}" for j in range(len(new_row))]
        output.append(new_row)

output = pd.DataFrame(output).reset_index(drop=True)
output.columns = output.iloc[0]
output = output[1:].reset_index(drop=True)