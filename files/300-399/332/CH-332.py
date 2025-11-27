import pandas as pd
from datetime import timedelta

path = "300-399/332/CH-332 Date Calculation.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=7)
test = pd.read_excel(path, usecols="D", skiprows=1, nrows=7)
test['End Time'] = pd.to_datetime(test['End Time'] , format="%d/%m/%Y - %H:%M:%S")

input['Start Date'] = pd.to_datetime(input['Start Date'], format="%d/%m/%Y - %H:%M:%S")
# durarion + start date
input['Calculated End Date'] = input.apply(lambda row: row['Start Date'] + timedelta(hours=row['Duration [h]']), axis=1)

print(input['Calculated End Date'].equals(test['End Time']))  # First entry wrong