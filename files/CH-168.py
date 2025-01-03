import pandas as pd

path = "CH-168 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=25)
test = pd.read_excel(path, usecols="G:I", skiprows=1, nrows=25).rename(columns=lambda x: x.split('.')[0])

input['Group'] = ((input['Stock price'].cummin() != input['Stock price'].cummin().shift().fillna(input['Stock price'].cummin().iloc[0])).cumsum() + 1)

print(all(input == test)) # True