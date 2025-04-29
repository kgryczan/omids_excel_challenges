import pandas as pd

path = "CH-226 Column Splitting.xlsx"

input_data = pd.read_excel(path, usecols="B", skiprows=1, nrows=6)
test_data = pd.read_excel(path, usecols="D:F", skiprows=1, nrows=6)

input_data[["ID.1", "ID.2", "ID.3"]] = input_data["ID"].str.split(r"(?<=[A-Za-z])(?=[A-Za-z])", expand=True)
input_data = input_data.drop(columns=["ID"])
print(input_data)