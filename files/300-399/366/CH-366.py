import pandas as pd

path = "300-399/366/CH-366 Text Cleaning.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=2, nrows=7)
test = pd.read_excel(path, usecols="E", skiprows=2, nrows=7).astype(str)

input["ID"] = input["ID"].astype(str).str.replace(r"(.)\1+", r"\1", regex=True)

print(input["ID"].equals(test['ID.1'])) # True
