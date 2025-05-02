import pandas as pd
from dateutil.parser import parse

path = "CH-183 Match the Dates.xlsx"

input = pd.read_excel(path, usecols="C", skiprows=1, nrows=28)
test = pd.read_excel(path, usecols="I", skiprows=1, nrows=12).rename(columns=lambda x: x.split('.')[0])

def parse_date(date_str):
    try:
        return parse(date_str, fuzzy=True, yearfirst=True)
    except ValueError:
        return None

input['Parsed Date'] = input.iloc[:, 0].apply(parse_date).dt.date
result = pd.DataFrame(input['Parsed Date'].drop_duplicates().unique(), columns=['Date'])

print(all(result['Date'] == test['Date'])) # True