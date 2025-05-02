import pandas as pd
import re

path = "CH-216 Column Splitting.xlsx"

input = pd.read_excel(path, usecols="B", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="D:F", skiprows=1, nrows=6)
result = input["ID"].str.extract(r"^([A-Z]{2})(.*)([A-Za-z0-9]{1})$")
result.columns = ["Prefix", "Root", "Suffix"]

