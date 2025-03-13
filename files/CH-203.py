import pandas as pd
import numpy as np

path = "CH-203 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=61)
test = pd.read_excel(path, usecols="G:H", skiprows=1, nrows=3)

input['Date'] = pd.to_datetime(input['Date'])
input = input.set_index('Date').asfreq('D', fill_value=0).reset_index()
input['wday'] = input['Date'].dt.day_name()
input['Group'] = input['Date'].dt.strftime('%b')

result_summary = (input.query("wday not in ['Saturday', 'Sunday'] and Sales == 0")
                  .groupby('Group').size().reset_index(name='No missing dates')
                  .sort_values('No missing dates').reset_index(drop=True))

print(test['No missing dates'].equals(result_summary['No missing dates']))