import pandas as pd
import re
import string

path = "400-499/434/CH-434 Replacement.xlsx"
input = pd.read_excel(path, usecols="B:D", nrows=7, skiprows=2)
test = pd.read_excel(path, usecols="F:H", nrows=7, skiprows=2)
test.columns = input.columns

punct = re.escape(string.punctuation)
pattern = rf"(?<!R)[{punct}]|[{punct}](?!S)"

result = input.copy()
result["Product ID"] = result["Product ID"].str.replace(pattern, "-", regex=True)

print(result.equals(test))
# True
