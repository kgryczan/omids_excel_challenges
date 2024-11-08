import pandas as pd
from pandas.tseries.offsets import Day

path = "CH-140 Golden Period.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=25)
test = pd.read_excel(path, usecols="F:H", skiprows=1, nrows=3).rename(columns=lambda x: x.split('.')[0])

result = input.groupby(['Date', 'Customer'], as_index=False)['Qty'].sum()
result = (result.set_index('Date')
          .groupby('Customer')
          .apply(lambda x: x.reindex(pd.date_range(x.index.min(), "2024-11-01", freq='D')))
          .reset_index(level=0, drop=True)
          .reset_index())
result['Qty'] = result['Qty'].fillna(0)
result['Customer'] = result['Customer'].ffill()
result['rolling_sum'] = result.groupby('Customer')['Qty'].rolling(window=10, min_periods=10).sum().reset_index(level=0, drop=True)
result = result[result.groupby('Customer')['rolling_sum'].transform('max') == result['rolling_sum']]
result = result.groupby('Customer').tail(1)
result['min_date'] = (result['index'] - Day(9)).dt.strftime('%y-%m-%d')
result['Date'] = result['index'].dt.strftime('%y-%m-%d')
result['Period'] = result['min_date'] + ' to ' + result['Date']
result = result[['Customer', 'Period', 'rolling_sum']].rename(columns={'rolling_sum': 'Total Qty'}).reset_index(drop=True)
result['Total Qty'] = result['Total Qty'].astype('int64')

print(result.equals(test)) # True
