import pandas as pd

path = "CH-079 Remove Blank Columns.xlsx"

input = pd.read_excel(path, usecols="B:I", skiprows=1)
test  = pd.read_excel(path, usecols="K:N", skiprows=1)
test.columns = test.columns.str.replace('.1', '')

result = input.loc[:, input.columns[~input.isnull().all()]]
print(result.equals(test)) # True