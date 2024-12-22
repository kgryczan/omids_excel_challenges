import pandas as pd
import re

path = "CH-162 Extract from Text.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="E:I", skiprows=1, nrows=6)

def clean_value(value):
    value = re.sub(r"(\d),\{", r"\1},{", value)
    value = re.sub(r"\{+", "{", value)
    value = re.sub(r"\}+", "}", value)
    return value

input['Value'] = input['Value'].apply(clean_value)
input = input.assign(Value=input['Value'].str.split(r"(?<=\}),(?=\{)")).explode('Value')
input['rn'] = input.groupby('ID').cumcount() + 1
r1 = input.pivot(index='ID', columns='rn', values='Value').reset_index()
r1.columns = test.columns

print(r1.equals(test)) # True