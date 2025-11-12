import pandas as pd

path = "300-399/325/CH-325 Date Calculation.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=7)
test = pd.read_excel(path, usecols="D:D", skiprows=1, nrows=7)\
    .assign(**{"End Time": lambda df: pd.to_datetime(df["End Time"], dayfirst=True)})

input['Start Date'] = pd.to_datetime(input['Start Date'], dayfirst=True)
input['Duration [h:m:s]'] = pd.to_timedelta(input['Duration [h:m:s]'])
input['End Time Calc'] = input['Start Date'] + input['Duration [h:m:s]']

print(input['End Time Calc'] == test['End Time']) # One result incorect
