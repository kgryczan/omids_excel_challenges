import pandas as pd

path = "300-399/394/CH-394 Filter.xlsx"
input = pd.read_excel(path, usecols="B", nrows=8, skiprows=2)
test = pd.read_excel(path, usecols="F", nrows=4, skiprows=2)

result = input[input['ID'].str.contains(r'[A-Z]{2}[1-6]{3,4}|[A-Z]{2}[7-9]{3,4}')].reset_index(drop=True)
print(result['ID'].equals(test['ID.1']))
# [1] True