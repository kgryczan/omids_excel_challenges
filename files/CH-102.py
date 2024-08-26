import pandas as pd
import numpy as np

path = "CH-102 Compare Rows.xlsx"
input = pd.read_excel(path, usecols = "B:C", skiprows = 1)
test  = pd.read_excel(path, usecols = "G", skiprows = 1, nrows = 12)

result = input.where(input["Sales"] - input["Sales"].shift(1) > 0).dropna().reset_index(drop = True)
result = result["Date"].rename("Dates")
print(result.equals(test["Dates"])) # True

# II Aproach with no comparison using > or < operators

result = input.where(np.sign(input["Sales"] - input["Sales"].shift(1)) == 1).dropna().reset_index(drop = True)
result = result["Date"].rename("Dates")
print(result.equals(test["Dates"])) # True

# be careful and call only first or second approach. :D