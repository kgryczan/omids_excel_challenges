import pandas as pd
import numpy as np

path = "CH-109 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1)
test  = pd.read_excel(path, usecols="G:H", skiprows=1, nrows = 8)

result = input.assign(group = input['Sales'].lt(input['Sales'].shift().fillna(input['Sales'].iloc[0])).cumsum(),
                      Date = input['Date'].dt.strftime("%m/%d/%Y")).groupby('group').agg(range=('Date', lambda x: f"{x.min()}-{x.max()}"),
                                                                                       Total_Sales=('Sales', 'sum')).reset_index()

print(result["Total_Sales"].equals(test["Total Sales"])) # True