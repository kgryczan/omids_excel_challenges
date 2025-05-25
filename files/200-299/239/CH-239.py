import pandas as pd
import re

path = "200-299/239/CH-239 Extract from Text.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=5)
test = pd.read_excel(path, usecols="D", skiprows=1, nrows=10)

result = input.assign(
    **{'Product ID': input['Text'].apply(lambda x: re.findall(r'[a-zA-Z]{2}[0-9]{1}-[0-9]{2}', str(x)))}
).explode('Product ID').drop(
    columns='Text'
).reset_index(drop=True)

print(result.equals(test)) # True