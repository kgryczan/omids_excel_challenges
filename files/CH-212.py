import pandas as pd

path = "CH-212 Remove duplicate.xlsx"

input = pd.read_excel(path, usecols="B:E", skiprows=1, nrows=15).values.flatten()
test = pd.read_excel(path, usecols="G", skiprows=1, nrows=10).values.flatten()

input = pd.Series(input).drop_duplicates(keep=False).values

print(input)
# Values for X-022 and X-025 are not proper solutions. 
