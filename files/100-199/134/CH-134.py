import pandas as pd

path = "CH-134 Final Week of the Month.xlsx"
input = pd.read_excel(path, usecols= "C:E", skiprows= 1, nrows= 27)
test = pd.read_excel(path, usecols="G:I", skiprows=1, nrows=3).rename(columns=lambda x: x.split('.')[0])
 
input['Date'] = pd.to_datetime(input['Date'])
input['EoM'] = input['Date'] + pd.offsets.MonthEnd(0)
input = input[input['EoM'] - input['Date'] < pd.Timedelta(days=7)]

result = input[["Date","Product","Qty"]].reset_index(drop=True)

print(result.equals(test)) # True
