import pandas as pd

path = "200-299/250/CH-250  Hierarchical Structure from ID Codes.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=9)
test = pd.read_excel(path, usecols="E:H", skiprows=1, nrows=5)

lookup = dict(zip(input["ID"], input["ParentID"]))
def get_path(id, path=None):
    if path is None:
        path = []
    parent = lookup.get(id)
    if pd.isna(parent):
        return [id] + path
    else:
        return get_path(parent, [id] + path)

leaves = set(input["ID"]) - set(input["ParentID"].dropna())
paths = [get_path(leaf) for leaf in leaves]
max_len = max(len(p) for p in paths)
paths_padded = [p + [None] * (max_len - len(p)) for p in paths]
paths = pd.DataFrame(paths_padded, columns=[f"Level {i+1}" for i in range(max_len)])
print(paths)
