import pandas as pd

path = "200-299/252/CH-252 Switching Value.xlsx"
input = pd.read_excel(path, usecols="C:D", skiprows=1, nrows=8)
test = pd.read_excel(path, usecols="F:G", skiprows=1, nrows=8).rename(columns=lambda x: x.replace('.1', ''))

result = input.copy()
result['Importance'] = result['Importance'].str.strip().replace({
    "Very low": 1, "Low": 2, "Moderate": 3, "High": 4, "Very high": 5
})

print(result.equals(test)) # True