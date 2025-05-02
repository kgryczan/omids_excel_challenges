import pandas as pd

path = "CH-153 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=10)
test = pd.read_excel(path, usecols="G:H", skiprows=1, nrows=4).rename(columns=lambda x: x.split('.')[0])

input['dates'] = input.apply(lambda row: pd.date_range(start=row['From'], end=row['To']), axis=1)
dates = pd.to_datetime(input.explode('dates')['dates'].unique())
grouped_dates = pd.DataFrame({'dates': dates})
grouped_dates['group'] = (grouped_dates['dates'].diff().dt.days > 1).cumsum() + 1
grouped_dates = grouped_dates.groupby('group')['dates'].agg(['min', 'max']).reset_index()
grouped_dates = grouped_dates.rename(columns={'min': 'From', 'max': 'To'})[['From', 'To']]

print(grouped_dates.equals(test)) # True