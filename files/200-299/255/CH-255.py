import pandas as pd
import re

path = "200-299/255/CH-255 Parse HTML.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="D:G", skiprows=1, nrows=6)

def parse_markup(text):
    matches = re.findall(r"<([^>]+)>([^<]+)</\1>", str(text))
    return {tag: value for tag, value in matches}

parsed = input["Raw Text"].apply(parse_markup).apply(pd.Series)
result = pd.concat([input, parsed], axis=1).drop(columns=["Raw Text"])
result.columns = test.columns
result[["ID", "Value"]] = result[["ID", "Value"]].apply(pd.to_numeric, errors="coerce")

print(result.equals(test))