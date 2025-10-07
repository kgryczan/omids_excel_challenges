import pandas as pd

path = "300-399/307/CH-307 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=17)
test = pd.read_excel(path, usecols="G:H", skiprows=1, nrows=2)

result = (
    input.assign(Group=(input.index % 2) + 1)
    .groupby('Group', as_index=False)['Sales'].sum()
    .rename(columns={'Sales': 'Total Sales'})
)

print(result.equals(test)) # True
