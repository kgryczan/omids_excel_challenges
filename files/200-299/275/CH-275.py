import pandas as pd
import re

path = "200-299/275/CH-275 Text Matching.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=7)

input['chars_id'] = input.iloc[:,0].apply(lambda s: set(re.sub(r'[^A-Za-z0-9]', '', str(s))))

pairs = [
    {'ID 1': input.iloc[j, 0], 'ID 2': input.iloc[i, 0]}
    for i in range(len(input))
    for j in range(i+1, len(input))
    if len(input.at[i, 'chars_id'] & input.at[j, 'chars_id']) >= 3
]

result = pd.DataFrame(pairs)
print(result) # Correct pais in different order