import pandas as pd

path = "CH-205 Missing Char.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="D", skiprows=1, nrows=6)

def replace_slashes_with_indices(word):
    return ''.join(str(i + 1) if char == '/' else char for i, char in enumerate(word))

input['Modified'] = input.iloc[:, 0].apply(replace_slashes_with_indices)
