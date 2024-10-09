import re
import pandas as pd

path = "CH-125 Pad middle.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=8)
test = pd.read_excel(path, usecols="D", skiprows=1, nrows=8).rename(columns=lambda x: x.replace(".1", ""))

def innix_pad(string):
    letters, numbers = re.findall(r"[A-Z]+|[0-9]+", string)
    return f"{letters}{numbers.zfill(6 - len(letters))}"

input = input.map(innix_pad)

print(input.equals(test)) # True