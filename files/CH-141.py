import pandas as pd

path = "CH-141 Fill UP and Down.xlsx"
input = pd.read_excel(path, usecols="C:D", skiprows=1, nrows=12)

result = input.groupby('ID', group_keys=False).apply(lambda group: group.ffill().bfill()).reset_index(drop=True)

print(result)

# As result is not filled with numbers, but highlighted to show which value is proper.
# We need to validate it by eye, but it is correct.