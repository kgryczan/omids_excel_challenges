import pandas as pd

path = "CH-156 Column Splitting.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=7)
test = pd.read_excel(path, usecols="D:F", skiprows=1, nrows=7).fillna('')

def split_id(id):
    n = len(id)
    mid = n // 2
    if n % 2 == 0:
        id1, id2, id3 = id[:mid], id[mid:], None
    else:
        id1, id2, id3 = id[:mid], id[mid:mid + 1], id[mid + 1:]
    return pd.Series([id1, id2, id3])

result = input['ID'].apply(split_id).fillna('')
result.columns = ['ID.1', 'ID.2', 'ID.3']

# identical except one field wrong in given solution