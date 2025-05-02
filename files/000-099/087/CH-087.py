import pandas as pd

path = 'CH-087 Price List.xlsx'
input1 = pd.read_excel(path, usecols= "B:D", skiprows= 1, nrows = 7)
input2 = pd.read_excel(path, usecols= "G:I", skiprows= 1, nrows = 9)
input2.columns = input2.columns.str.replace(".1", "")
test = pd.read_excel(path, usecols= "J", skiprows= 1, nrows = 9)
test.columns = test.columns.str.replace(".1", "")

result = input2.merge(input1, on = "Product", how = "left")\
    .loc[lambda df: df['Date'] >= df['From Date']]\
    .groupby(['Product', 'Date']).max()\
    .sort_values(by = ['Date'], ascending = [True])\
    .reset_index()
    
print(result["Price"].equals(test["Price"])) # True