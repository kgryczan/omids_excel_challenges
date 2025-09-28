import pandas as pd

path = "300-399/302/CH-302 Remove Duplicate Values.xlsx"
input = pd.read_excel(path, usecols="B:E", skiprows=1, nrows=10)
test = pd.read_excel(path, usecols="G:J", skiprows=1, nrows=6).rename(columns=lambda col: col.replace('.1', ''))

input['all_sorted'] = input.filter(like="Value").apply(lambda r: ','.join(map(str, sorted(r))), axis=1)
result = input.drop_duplicates('all_sorted').drop('all_sorted', axis=1).reset_index(drop=True)

print(result.equals(test)) # True