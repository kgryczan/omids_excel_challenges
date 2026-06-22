import pandas as pd

path = "400-499/431/CH-431 Column Splitting.xlsx"
input = pd.read_excel(path, usecols="B", nrows=8, skiprows=2)
test = pd.read_excel(path, usecols="F:I", nrows=8, skiprows=2, dtype=str).fillna("")

seen = set()


def new_chars(s):
    global seen
    out = list(dict.fromkeys(c for c in s if c not in seen))
    seen |= set(out)
    return out


result = (
    pd.DataFrame(input["ID"].map(new_chars).tolist())
    .rename(columns=lambda x: f"ID{x + 1}")
    .where(pd.notna, "")
)

print(result.equals(test))
# True
