import pandas as pd
import re

path = "CH-218 Column Splitting.xlsx"
input_data = pd.read_excel(path, usecols="B", skiprows=1, nrows=6)
test_data = pd.read_excel(path, usecols="D:E", skiprows=1, nrows=6)

input_data["Uppercase"] = input_data["ID"].apply(lambda x: "".join(re.findall(r"[A-Z]+", x)))
input_data["Lowercase"] = input_data["ID"].apply(lambda x: "".join(re.findall(r"[a-z]+", x)))

print(input_data)