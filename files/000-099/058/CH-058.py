import pandas as pd
import numpy as np
input1 = pd.read_excel("CH-058 Stepped Tax.xlsx", usecols="B:D", skiprows=1, nrows = 6)
input2 = pd.read_excel("CH-058 Stepped Tax.xlsx", usecols="F:G", skiprows=1, nrows = 6)
test   = pd.read_excel("CH-058 Stepped Tax.xlsx", usecols="H", skiprows=1, nrows = 6)

input1.loc[4, 'To'] = float('inf')
input1['key'] = 1
input2['key'] = 1
output = pd.merge(input1, input2, on='key')
output['income_over_threshold'] = output["Income"] - output["From"]
output['income_in_threshold'] = np.where((output["Income"] >= output["From"]) & (output["Income"] <= output["To"]), True, False)
output = output[output['income_over_threshold'] > 0].sort_values(by = ["Person ID"]).reset_index(drop = True)
output['tax'] = np.where(output['income_in_threshold'], 
                         output['income_over_threshold'] * output['Tax Rate'], 
                         (output['To'] - output['From']) * output['Tax Rate'])
output = output.groupby('Person ID').agg({'tax': 'sum'}).astype("float64").reset_index()

output['tax'] = output['tax'].round(2)
test['tax'] = test['Tax'].round(2)

print(all(output['tax'] == test['tax'])) # True