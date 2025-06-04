import pandas as pd
import re

path = "200-299/244/CH-244 Column Splitting.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="D:E", skiprows=1, nrows=6)

def split_by_sec_del(text):
    if pd.isna(text): return [text, None]
    h = [m.start() for m in re.finditer("-", str(text))]
    s = [m.start() for m in re.finditer("/", str(text))]
    if sum(len(x) >= 2 for x in [h, s]) == 0: return [text, None]
    if h and s and len(h) >= 2 and len(s) >= 2:
        i = min(h[1], s[1])
    elif len(h) >= 2:
        i = h[1]
    else:
        i = s[1]
    return [text[:i], text[i+1:]]

split_cols = input.iloc[:, 0].apply(split_by_sec_del)
result = pd.DataFrame(split_cols.tolist(), columns=["ID.1", "ID.2"])

print(result.equals(test)) # True