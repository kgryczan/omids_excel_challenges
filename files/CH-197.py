import pandas as pd
import numpy as np

path = "CH-197 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=17)
test = pd.read_excel(path, usecols="G:H", skiprows=1, nrows=6)

input['Date'] = pd.to_datetime(input['Date'], format='%Y-%m-%d')
input = input.set_index('Date').reindex(pd.date_range(input['Date'].min(), input['Date'].max(), freq='D')).fillna(0).rename_axis('Date').reset_index()

input['Group'] = np.where(input['Sales'] == 0, (input['Sales'] == 0).cumsum() % 2, np.nan)
input['Group'] = input.groupby('Group').cumcount() + 1
input['Group'] = input['Group'].replace(0, np.nan).fillna(method='bfill').fillna(input['Group'].max() + 1)

result = input.groupby('Group').agg({'Sales': 'sum'}).reset_index().rename(columns={'Sales': 'Total Sales'})

#    Group  Total Sales
# 0    1.0        137.0
# 1    2.0         27.0
# 2    3.0         89.0
# 3    4.0         51.0
# 4    5.0         53.0
# 5    6.0          0.0
# 6    7.0         23.0