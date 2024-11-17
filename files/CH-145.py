import pandas as pd
import re

path = "CH-145 Length of Pattern.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=30)
test = pd.read_excel(path, usecols="F:G", skiprows=1, nrows=3).rename(columns=lambda x: x.split('.')[0])

def largest_length(result):
    patterns = re.findall(r"(?:\+\+-)+(?:\+)?", result)
    return max(map(len, patterns), default=0)

input['Result'] = input.groupby('Product')['Result'].transform(lambda x: ''.join(x))
input = input.drop_duplicates(subset=['Product'])
input['Largest Length'] = input['Result'].apply(largest_length)
result = input[['Product', 'Largest Length']].reset_index(drop=True)

print(result.equals(test)) # True