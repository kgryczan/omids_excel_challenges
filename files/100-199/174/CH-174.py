import pandas as pd

path = "CH-174 Filtering.xlsx"
input = pd.read_excel(path, usecols="C:D", skiprows=1, nrows=24, names=['Index', 'Value'])
test = pd.read_excel(path, usecols="F:G", skiprows=1, nrows=5, names=['Index', 'Value'])

def filter_values(df):
    df['All_Lagged_Lead_Lower'] = (df['Value'].shift(1, fill_value=0) < df['Value']) & \
                                  (df['Value'].shift(2, fill_value=0) < df['Value']) & \
                                  (df['Value'].shift(-1, fill_value=0) < df['Value']) & \
                                  (df['Value'].shift(-2, fill_value=0) < df['Value'])
    return df[df['All_Lagged_Lead_Lower']][['Index', 'Value']]

result = filter_values(input).reset_index(drop=True)
print(result.equals(test)) # True
