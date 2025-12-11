import pandas as pd
import re

path = "300-399/339/CH-339 Column Splitting.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=2, nrows=6, dtype=str)
test = pd.read_excel(path, usecols="F:H", skiprows=2, nrows=6, dtype=str)

input["ID"] = input["ID"].str.replace(r"([A-Za-z]{2})([0-9]{2})", r"\1|\2", regex=True)
split_cols = input["ID"].str.split("|", expand=True)
split_cols.columns = [f"ID {i+1}" for i in range(split_cols.shape[1])]

print(split_cols.equals(test)) # True
