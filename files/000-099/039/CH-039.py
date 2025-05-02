import pandas as pd

input = pd.read_excel("CH-039 Transformation.xlsx", sheet_name="Sheet1", usecols="B:E", nrows=9)
test  = pd.read_excel("CH-039 Transformation.xlsx", sheet_name="Sheet1", usecols="G",  nrows=22)

input = input.stack().reset_index(drop=True)
input = input.sort_values().drop_duplicates().reset_index(drop=True)
input = pd.DataFrame(input, columns=['result'])

print(input['result'].equals(test['Result - Unique Code'])) # True