import pandas as pd

path = "400-499/401/CH-401 Column Splitting.xlsx"
input = pd.read_excel(path, usecols="B", nrows=6, skiprows=2)
test = pd.read_excel(path, usecols="F:H", nrows=6, skiprows=2)
test = test.fillna("").astype(str)

def split_id(x):
	x = str(x)
	n = len(x)
	q = n // 3
	r = n % 3
	lengths = [q + (1 if r > 0 else 0), q + (1 if r > 1 else 0), q]
	k1 = lengths[0]
	k2 = lengths[0] + lengths[1]
	return {
		"ID1": x[:k1],
		"ID2": x[k1:k2],
		"ID3": x[k2:n],
	}
id_col = "ID" if "ID" in input.columns else input.columns[0]
result = pd.DataFrame(input[id_col].apply(split_id).tolist())

print(result.equals(test))
# one cell has different value.