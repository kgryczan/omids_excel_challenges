import pandas as pd

path = "300-399/351/CH-351 Filter.xlsx"
input_data = pd.read_excel(path, usecols="B", skiprows=2, nrows=8)
test_data = pd.read_excel(path, usecols="F", skiprows=2, nrows=3).rename(columns=lambda x: x.rstrip('.1'))

result = input_data[input_data.iloc[:, 0].str.contains(r"M.*N.*M.*", na=False)].reset_index(drop=True)

print(result.equals(test_data)) # True