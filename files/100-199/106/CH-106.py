import pandas as pd 

path = "CH-106 Custom Rank.xlsx"
input = pd.read_excel(path, usecols="C:G", skiprows=1)
test  = pd.read_excel(path, usecols="L:M", skiprows=1)
test.columns = test.columns.str.replace(".1", "")

result = input.set_index(["Gold", "Silver", "Bronze"])
result = result.sort_index(ascending=[False, False, False]).reset_index()

print(result["Country"].equals(test["Country"])) # True
