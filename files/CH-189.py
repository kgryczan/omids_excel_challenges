import pandas as pd

path = "CH-189 Combining the columns.xlsx"
input = pd.read_excel(path, usecols="B:E", skiprows=1, nrows=6)

def replace_pattern(row):
    return ''.join(row['First Name'] if c == 'F' else row['Last Name'] if c == 'L' else row['Middle Name'] if c == 'M' else c for c in row['Pattern'].strip())

input['Custom Format'] = input.apply(replace_pattern, axis=1)
result = input.groupby('First Name')['Custom Format'].apply(''.join).reset_index()

print(result)
