import pandas as pd

path = "200-299/273/CH-273 Advanced Sorting.xlsx"
input = pd.read_excel(path,usecols="B:E", skiprows = 1, nrows=8)
test = pd.read_excel(path, usecols="G:J", skiprows=1, nrows=8).rename(columns=lambda col: str(col).replace('.1', ''))

cols_2 = [col for col in input.columns if str(col).startswith('2')]
input = (
    input.assign(
        RowMax=input[cols_2].max(axis=1),
        RowMaxPos=input[cols_2].idxmax(axis=1).map(lambda col: input.columns.get_loc(col) + 1)
    )
    .sort_values(['RowMax', 'RowMaxPos'], ascending=[False, False])
    .drop(['RowMax', 'RowMaxPos'], axis=1)
    .reset_index(drop=True)
)

print(input.equals(test)) # True