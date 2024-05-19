import pandas as pd
from pandas.tseries.offsets import MonthEnd

input = pd.read_excel("CH-054 Missing Values.xlsx",  usecols="B:D", skiprows=1, nrows = 19)
test = pd.read_excel("CH-054 Missing Values.xlsx",  usecols="H:J", skiprows=1)
test.columns = test.columns.str.replace(".1", "")

input["Date"] = pd.to_datetime(input["Date"])
test["Date"] = pd.to_datetime(test["Date"])
input['Date'] = input['Date'] - MonthEnd(0) 
input = input.set_index('Date').groupby('Project').apply(lambda group: group.asfreq('M')).reset_index(level=0, drop=True).reset_index()
input['Actual Progress'] = input.groupby('Project')['Actual Progress'].fillna(method='ffill')
input['Date'] = input['Date'] + MonthEnd(0) 
input['Project'] = input['Project'].fillna(method='ffill')
input = input.fillna(method='ffill')

print(input.equals(test)) # True