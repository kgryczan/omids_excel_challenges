import pandas as pd

path = "CH-227 Data Normalization Min-Max.xlsx"

input = pd.read_excel(path, usecols="B:G", skiprows=1, nrows=7)
test = pd.read_excel(path, usecols="J:O", skiprows=1, nrows=7).rename(columns=lambda col: col.split('.1')[0] if '.1' in col else col)

result = (input - input.min()) / (input.max() - input.min())

print(result.equals(test)) # True