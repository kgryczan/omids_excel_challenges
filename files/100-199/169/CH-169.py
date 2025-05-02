import pandas as pd
import re

path = "CH-169 Extract From Text Part 2.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="D", skiprows=1, nrows=6)

def extract_text(text):
    pattern = r"(?<=\{)[^{}]+(?=\})|(?<=\[)[^\]]+(?=\])|(?<=\()[^\)]+(?=\))|(?<=\*)[^\*]+(?=\*)"
    matches = re.findall(pattern, text)
    return ", ".join(matches)

input['result'] = input['Text'].apply(extract_text)
 
print(input["result"].equals(test["Extracted"])) # True