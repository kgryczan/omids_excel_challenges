import pandas as pd

path = "400-499/441/CH-441 Column Splitting.xlsx"
input = pd.read_excel(path, usecols="B", nrows=9, skiprows=2)
test = pd.read_excel(path, usecols="F:I", nrows=9, skiprows=2, dtype="str")
test = test.fillna("")

seen = set()
rows = []
for value in input["ID"]:
    chars = [x for x in dict.fromkeys(value) if x not in seen]
    seen.update(value)
    rows.append(chars)
result = pd.DataFrame(rows).rename(columns=lambda x: f"ID{x + 1}")
result = result.fillna("")

print(result.equals(test))
# True
