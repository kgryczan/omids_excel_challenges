import pandas as pd
import numpy as np

path = 'CH-097 Linear Interpolation.xlsx'
input = pd.read_excel(path, usecols = "B:E", skiprows = 1, nrows = 3)
test  = pd.read_excel(path, usecols = "H:K", skiprows = 1, nrows = 13) 
test.columns = ['Year', 'A', 'B', 'C']

years = pd.DataFrame({'Year': range(2010, 2023)})
r1 = years.merge(input, how='left', on='Year')

r1[['A', 'B', 'C']] = r1[['A', 'B', 'C']].interpolate().round().astype(int)

r1.iloc[[0, -1], 1:] = 2 * r1.iloc[[1, -2], 1:] - r1.iloc[[2, -3], 1:]
print(r1.equals(test)) # True