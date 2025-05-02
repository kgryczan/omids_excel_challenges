import pandas as pd
import re

path = "CH-078 Extract from Text 2.xlsx"

input = pd.read_excel(path, usecols="B", header=None, skiprows=2, nrows=1).iloc[0, 0]

test = pd.read_excel(path, usecols="B", skiprows=5, nrows=6)
test["Email Address"] = test["Email Address"].str[3:]
test = test.sort_values(by="Email Address").reset_index(drop=True)

patterns = [
    r"\d{4}-\d{2}-\d{2}",
    r"\d{2}\/\d{2}\/\d{4}",
    r"\b\w+ \d{1,2}[a-z]*?(?: to \w+ \d{1,2}[a-z]*)?, \d{4}\b"
]

result = pd.DataFrame()
for pattern in patterns:
    result = result.append(pd.DataFrame(re.findall(pattern, input), columns=["Email Address"]))
result = result.sort_values(by="Email Address").reset_index(drop=True)

print(result.equals(test))  # True
