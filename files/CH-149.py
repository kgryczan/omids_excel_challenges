import pandas as pd

path = "CH-149 Extract From Text.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="D", skiprows=1, nrows=6)

input['Extracted'] = input.iloc[:, 0].str.extract(r'(?<=[\(\[\{\*])(.*?)(?=[\)\]\}\*])', expand=False).fillna('')
input = input.drop(columns="Text")

print(input.equals(test)) # Test