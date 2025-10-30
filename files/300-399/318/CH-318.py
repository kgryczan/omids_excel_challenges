import pandas as pd
import numpy as np

path = "300-399/318/CH-318 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="B:E", skiprows=1, nrows=9, header=None).to_numpy()
test = pd.read_excel(path, usecols="G:J", skiprows=1, nrows=5).rename(columns=lambda c: c.replace('.1', ''))  

m = np.where(np.char.startswith(input.astype(str), 'Column'), np.nan, input)

for j in range(m.shape[1]):
    col = m[:, j][~pd.isna(m[:, j])]
    m[:len(col), j] = col
    m[len(col):, j] = np.nan

result = pd.DataFrame(m, columns=test.columns)
result = result.iloc[1:][~pd.isna(result['Date'])].reset_index(drop=True)
if 'Date' in result.columns:
    result['Date'] = pd.to_datetime(result['Date']).dt.strftime('%Y-%m-%d %H:%M')

print((result == test).all().all())
