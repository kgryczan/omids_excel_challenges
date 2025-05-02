import pandas as pd

path = "CH-206 Column Splitting.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="D:E", skiprows=1, nrows=6)

def split_even_odd_chars(series):
    return series.apply(lambda x: pd.Series([''.join(str(x)[::2]), ''.join(str(x)[1::2])], index=['Odd Positions', 'Even Positions']))

result = split_even_odd_chars(input.iloc[:, 0])


print(test)
print(result)