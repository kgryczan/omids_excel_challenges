import pandas as pd
import re

path = "300-399/377/CH-377 Filter.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=2, nrows=8)
test = pd.read_excel(path, usecols="F", skiprows=2, nrows=5).rename(columns=lambda c: re.sub(r"\.\d+$", "", c))

def digit_sum(ids, pat):
    return [sum(int(d) for d in re.findall(pat, x)) for x in ids]

result = input.copy()
result["even_sum"] = digit_sum(result["ID"], r"[02468]")
result["odd_sum"]  = digit_sum(result["ID"], r"[13579]")
result = result[result["even_sum"].lt(10) ^ result["odd_sum"].gt(10)][["ID"]]

print(result.equals(test))
# ST2467 doesn't match conditions.