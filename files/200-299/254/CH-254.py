import pandas as pd

path = "200-299/254/CH-254 Column Splitting.xlsx"
input_df = pd.read_excel(path, usecols="B", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="D:I", skiprows=1, nrows=6).fillna("")

def split_id(id_):
    parts = id_.split('-')
    n = len(parts)
    mid = (n + 1) // 2
    first = parts[:mid]
    second = parts[mid:]
    first += [''] * (3 - len(first))
    second = [''] * (3 - len(second)) + second
    return first + second

result = input_df.iloc[:,0].apply(split_id)
result = pd.DataFrame(result.tolist(), columns=[f'ID.{i}' for i in range(1,7)])
result = result.astype(str)
test = test.astype(str)

print(result.equals(test)) # True
