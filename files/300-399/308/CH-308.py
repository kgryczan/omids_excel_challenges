import pandas as pd
import re

path = "300-399/308/CH-308 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=2)
test = pd.read_excel(path, usecols="B:C", skiprows=5, nrows=24)

all_extracted = sum(
    input['Info'].apply(
        lambda x: re.findall(r"\d{4}/\d{1}/\d{1,2}/\d{2}", str(x))
    ).tolist(),
    []
)
split = pd.DataFrame(
    [x.split('/') for x in all_extracted],
    columns=['Year', 'Month', 'Day', 'Sale']
).astype(int)
split['Date'] = pd.to_datetime(split[['Year', 'Month', 'Day']])
result = split[['Date', 'Sale']]

print(result.equals(test)) # True