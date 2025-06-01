import pandas as pd

path = "200-299/243/CH-243 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=14)
test = pd.read_excel(path, usecols="F:G", skiprows=1, nrows=5)

input['Age Group'] = pd.cut(
    input['Age'],
    bins=[0, 30, 40, 50, 60, float('inf')],
    right=False,
    labels=["<30", "[30-40)", "[40-50)", "[50-60)", ">60"]
)

result = (
    input.groupby('Age Group')
    .size()
    .reindex(["<30", "[30-40)", "[40-50)", "[50-60)", ">60"], fill_value=0)
    .reset_index(name='Count')
)
result['Age Group'] = result['Age Group'].astype(str)

print(result.equals(test)) # True