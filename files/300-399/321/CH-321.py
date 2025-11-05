import pandas as pd
import numpy as np

path = "300-399/321/CH-321 Correlation.xlsx"
input1 = pd.read_excel(path, usecols="B:F", skiprows=1, nrows=6)
input2 = pd.read_excel(path, usecols="B:E", skiprows=12, nrows=7).sort_values('Year')
test = pd.read_excel(path, usecols="H:L", skiprows=1, nrows=3).rename(columns=lambda c: c.replace('.1', ''))
test = test.rename(columns={test.columns[0]: "Y"}).set_index("Y")
test.index.name = None

mer = pd.merge(input1, input2, on='Year', how='inner')
corr = mer.corr().loc[['Y1', 'Y2', 'Y3'],['X1', 'X2', 'X3', 'X4']]

# Replace .equals with np.allclose for near equality
print(np.allclose(corr.values, test.values, atol=1e-8)) 