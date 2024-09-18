import pandas as pd

path = "CH-115 Multi Replacement.xlsx"
input = pd.read_excel(path, usecols="B:E", skiprows=1)
test = pd.read_excel(path, usecols="G:J", skiprows=1).rename(columns=lambda x: x.replace(".1", ""))

result = input.replace({"0{3}|q": "-"}, regex=True)

print(result.equals(test))  # True