import pandas as pd
import re

path = "CH-215 Missing Char.xlsx"

input = pd.read_excel(path, usecols="B", skiprows=1, nrows=5)
test = pd.read_excel(path, usecols="D", skiprows=1, nrows=5).rename(columns=lambda x: re.sub(r"\.1$", "", x))

input["rn"] = range(1, len(input) + 1)
input = input.assign(ID=input["ID"].str.split("").apply(lambda x: [c for c in x if c != ""]))

def replace_non_alphanum_with_order(char_list):
    non_alpha_count = 0
    result = [
        (str(non_alpha_count := non_alpha_count + 1) if not char.isalnum() else char)
        for char in char_list
    ]
    return result

input["ID"] = input["ID"].apply(lambda x: "".join(replace_non_alphanum_with_order(x)))
input.drop(columns=["rn"], inplace=True)

print(input.equals(test)) # True