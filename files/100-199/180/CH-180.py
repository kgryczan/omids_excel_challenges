import pandas as pd 
from itertools import groupby
from operator import itemgetter

path = "CH-180 Hierarchical Structure.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=11)
test = pd.read_excel(path, usecols="E:F", skiprows=1, nrows=13)
test['Code'] = test['Code'].astype(str)

def get_hierarchical_code(data, target, root="A"):
    data = sorted([(str(parent), str(child)) for parent, child in data], key=itemgetter(0))
    children_by_parent = {k: list(map(itemgetter(1), g)) for k, g in groupby(data, key=itemgetter(0))}
    path = target
    code = []
    while path != root:
        parent = next((parent for parent, children in data if path in children), None)
        if parent is None:
            raise ValueError(f"Parent for node '{path}' not found. Check the hierarchy.")
        siblings = children_by_parent[parent]
        position = siblings.index(path) + 1
        code.insert(0, str(position))
        path = parent
    code.insert(0, "1")
    return "-".join(code)

unique_values = pd.unique(input.values.ravel())
hierarchical_codes = [get_hierarchical_code(input.values, value) for value in unique_values]
df = pd.DataFrame({ 'Code': hierarchical_codes, 'IDs': unique_values})
print(df.equals(test)) # True
    