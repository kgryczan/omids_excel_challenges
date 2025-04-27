import pandas as pd
from pandas import to_datetime

path = "CH-225 Date Range.xlsx"

start = pd.read_excel(path, usecols="C", skiprows=2, nrows=1, header=None).iloc[0, 0]
end = pd.read_excel(path, usecols="C", skiprows=3, nrows=1, header=None).iloc[0, 0]
step = pd.read_excel(path, usecols="C", skiprows=4, nrows=1, header=None).iloc[0, 0]

test = pd.read_excel(path, usecols="E", skiprows=1, nrows=11).assign(Dates=lambda df: pd.to_datetime(df['Dates']))

result = pd.DataFrame({'Dates': pd.date_range(start=start, end=end, freq=f"{step}D")})

print(result.equals(test)) # True if the result matches the test data