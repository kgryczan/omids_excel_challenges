import pandas as pd
import re

path = "CH-132 Merge.xlsx"

input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=5)
input2 = pd.read_excel(path, usecols="H:H", skiprows=1, nrows=7)
test = pd.read_excel(path, usecols="I:I", skiprows=1, nrows=7).rename(columns=lambda x: x.replace('.1', '')).sort_values(by='Value', ascending=False).reset_index(drop=True)

result = input.merge(input2, how='cross')
result['Match'] = result.apply(lambda x: bool(re.search(x['Sub code'], x['Code'])), axis=1)
result = result[result['Match']].sort_values(by='Value', ascending=False).reset_index(drop=True)[['Value']]
 
print(result.equals(test)) # True
