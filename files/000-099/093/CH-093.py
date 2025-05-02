import pandas as pd

path = "CH-093 Random Selection.xlsx"
input = pd.read_excel(path, usecols= "B:C", skiprows=1)

result = input.groupby("Department").apply(lambda x: x.sample(1)).reset_index(drop=True)

#    Department Staff ID
# 0          HR     S_01
# 1          IT     S_12
# 2   Marketing     S_03
# 3  Production     S_16
# 4         R&D     S_14