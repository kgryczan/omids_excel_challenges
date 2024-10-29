import pandas as pd
import re

path = "CH-135 Identify the Pattern.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=31)
test = pd.read_excel(path, usecols="F:G", skiprows=1, nrows=3).rename(columns=lambda x: x.split('.')[0])

def count_occurrences(string, pattern="+-+"):
    return sum(1 for i in range(len(string) - len(pattern) + 1) if string[i:i + len(pattern)] == pattern)

grouped = input.groupby("Product")["Result"].agg(''.join).reset_index()
grouped['Number of repitation'] = grouped['Result'].apply(count_occurrences)
grouped.drop(columns="Result", inplace=True)

print(grouped.equals(test)) # True