import pandas as pd

path = "CH-212 Remove duplicate.xlsx"

input = pd.read_excel(path, usecols="B:E", skiprows=1, nrows=15)
test = pd.read_excel(path, usecols="G", skiprows=1, nrows=9).sort_values(by="Item Code").reset_index(drop=True)

value_counts = input.melt(var_name="Column Title", value_name="Value") \
    .groupby("Value")["Column Title"].nunique() \
    .reset_index(name="Unique Column Titles") \
    .query("`Unique Column Titles` == 1") \
    .reset_index(drop=True)[["Value"]] \
    .rename(columns={"Value": "Item Code"})

print(value_counts.equals(test)) # True