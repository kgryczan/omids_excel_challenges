import pandas as pd

path = "400-499/421/CH-421 Column Splitting.xlsx"
input = pd.read_excel(path, usecols="B", nrows=7, skiprows=2)
test = pd.read_excel(path, usecols="F:J", nrows=7, skiprows=2)


def _char_counts(x):
	if pd.isna(x):
		return []
	s = str(x)
	chars = list(dict.fromkeys(s))
	return [f"{ch}:{s.count(ch)}" for ch in chars]


id_col = "ID" if "ID" in input.columns else input.columns[0]
result = input[id_col].map(_char_counts).apply(pd.Series)
result = result.rename(columns=lambda c: f"ID{c + 1}")

print(result.equals(test))
# True