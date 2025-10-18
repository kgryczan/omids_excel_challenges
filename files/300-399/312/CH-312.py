import pandas as pd
import numpy as np

path = "300-399/312/CH-312 Remove Duplicate Values.xlsx"
input = pd.read_excel(path, usecols="B:E", skiprows=1, nrows=10)
test = pd.read_excel(path, usecols="G:J", skiprows=1, nrows=5).rename(columns=lambda c: c.replace('.1', ''))

cols = [c for c in input.columns if c != "ID"]
input["set"] = input[cols].apply(lambda r: tuple(sorted(set(v for v in r if pd.notnull(v)))), axis=1)
result = input.drop_duplicates("set").drop("set", axis=1).reset_index(drop=True)

print(result.equals(test))