import pandas as pd
import re

input = pd.read_excel('CH-043 Sort Table columns .xlsx', usecols="B:G", skiprows=1, nrows = 7)
test = pd.read_excel('CH-043 Sort Table columns .xlsx', usecols="J:O", skiprows=1, nrows = 7)
test.columns = test.columns.str.replace(r'\.1$', '', regex=True)
                     
result = input[['Regions'] + input.drop('Regions', axis=1).sum().sort_values(ascending=False).index.tolist()]

print(result.equals(test)) # True