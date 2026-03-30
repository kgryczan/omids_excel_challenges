import pandas as pd
import re

path = "300-399/389/CH-389 Replacement.xlsx"
input = pd.read_excel(path, usecols="B:E", nrows = 8, skiprows = 2)
test = pd.read_excel(path, usecols="G:J", nrows = 8, skiprows = 2).rename(columns=lambda c: re.sub(r"\.\d+$", "", c))

input['Date'] = pd.to_datetime(input['Date'])
dow = input['Date'].dt.weekday
offset_days = ((7 - dow) % 7).where(dow >= 5, 0)
offset = pd.to_timedelta(offset_days, unit='D')
input['Date'] = input['Date'] + offset

print(input == test)

# One result different.