import pandas as pd
import re

path = "200-299/236/CH-236 Column Splitting.xlsx"
input_df = pd.read_excel(path, usecols="B", skiprows=1, nrows=6)
test_df = pd.read_excel(path, usecols="D:F", skiprows=1, nrows=6).fillna("")

def split_id(s):
    s = str(s)
    if re.match(r"^[A-Za-z]{3}", s):
        return [s[:3], s[3:6], s[6:]]
    else:
        return [s, "", ""]

result = input_df['ID'].apply(split_id).apply(pd.Series)
result.columns = ['ID.1', 'ID.2', 'ID.3']

print(result.equals(test_df)) # True