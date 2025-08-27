import pandas as pd

path = "200-299/286/CH-286 Advanced Filtering.xlsx"
input = pd.read_excel(path, usecols="B:E", skiprows=1, nrows=8)
test = pd.read_excel(path, usecols="G", skiprows=1, nrows=2)['IDs'].tolist()

result = (
    input.melt(id_vars="ID")
         .groupby("value")["ID"].transform("count")
         .groupby(input.melt(id_vars="ID")["ID"]).sum()
         .loc[lambda x: x == 3]
         .index.tolist()
)

print(result)
print(test)
# should be 2,4, and provided answer is 2,5