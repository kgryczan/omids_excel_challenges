import pandas as pd

path = "200-299/293/CH-293 Advanced Sorting.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=7)
test = pd.read_excel(path, usecols="F:H", skiprows=1, nrows=7).rename(columns=lambda col: col.replace('.1', ''))

sizes = ["S", "M", "L", "XL", "XXL", "XXXL"]
result = input.sort_values("Size", key=lambda x: x.map({s: i for i, s in enumerate(sizes)})).reset_index(drop=True)

print(result.equals(test)) # True