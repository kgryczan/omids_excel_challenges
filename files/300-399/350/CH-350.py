import pandas as pd
import re
from itertools import combinations

path = "300-399/350/CH-350 Filter.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=2, nrows=8)
test = pd.read_excel(path, usecols="F", skiprows=2, nrows=3).rename(columns=lambda col: col.replace('.1', ''))

def check_pattern(text):
    chars = list(dict.fromkeys(str(text)))
    for p in combinations(chars, 2):
        pattern = f"{re.escape(p[0])}.*{re.escape(p[1])}.*{re.escape(p[0])}.*{re.escape(p[1])}"
        if re.search(pattern, str(text)):
            return True
    return False

result = input[input['ID'].apply(check_pattern)].reset_index(drop=True)

print(result.equals(test)) 
# True