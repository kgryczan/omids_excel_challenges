import pandas as pd

path = "CH-199 Combining the columns.xlsx"
input = pd.read_excel(path, usecols="B:E", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="H", skiprows=1, nrows=6)

def combine_columns(row):
    first_name, middle_name, last_name, pattern = row
    order = list(map(int, pattern.split(',')))
    names = [first_name, middle_name, last_name]
    return ' '.join([names[i-1] for i in order])

input['Custom Format'] = input.apply(combine_columns, axis=1)
result = input['Custom Format']

print(all(input['Custom Format'] == test['Custom Format'])) # True