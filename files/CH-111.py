import pandas as pd

path = "CH-111 iNCREASED SALES.xlsx"
input = pd.read_excel(path, usecols = "B:D", skiprows = 1, nrows = 24)
test  = pd.read_excel(path, usecols = "H", skiprows = 1, nrows = 4)
                      
result = input.groupby("Date").sum()
result = result[result["Sales"] > result["Sales"].shift(1)].reset_index()
result = result.drop(columns=["Sales", "Product"])

print(result["Date"].equals(test["Dates"])) # True