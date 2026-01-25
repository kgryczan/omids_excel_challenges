import pandas as pd

path = "300-399\\357\\CH-357 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="B:F", nrows = 11, skiprows = 2)
test = pd.read_excel(path, usecols="H:L", nrows = 5, skiprows = 2)

split_dfs, current_df = [], []

for _, row in input.iterrows():
    if row[0] == "Date" and current_df:
        split_dfs.append(pd.DataFrame(current_df, columns=input.columns))
        current_df = []
    current_df.append(row)

if current_df: 
    split_dfs.append(pd.DataFrame(current_df, columns=input.columns))

for i, df in enumerate(split_dfs):
    df.columns = df.iloc[0]
    split_dfs[i] = df[1:].reset_index(drop=True)

result_df = pd.concat(split_dfs, ignore_index=True)
result_df = result_df[['Date', 'A', 'B', 'C', 'D']]

print(all(result_df == test))
# True