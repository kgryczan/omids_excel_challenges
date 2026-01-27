import pandas as pd

path = "300-399\\358\\CH-358 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="B:E", nrows = 14, skiprows = 2)
test = pd.read_excel(path, usecols="G:K", nrows = 5, skiprows = 2)

split_dfs, cur_df = [], []
input.iloc[:, 0] = input.iloc[:, 0].fillna("Date")

for _, row in input.iterrows():
    if row.iloc[0] == "Date" and cur_df:
        split_dfs.append(pd.DataFrame(cur_df, columns=input.columns))
        cur_df = []
    cur_df.append(row)

if cur_df: 
    split_dfs.append(pd.DataFrame(cur_df, columns=input.columns))

for i, df in enumerate(split_dfs):
    df.columns = df.iloc[0]
    split_dfs[i] = df[1:].reset_index(drop=True)
    split_dfs[i] = split_dfs[i].dropna(axis=1, how='all')

final_dfs = []
for df in split_dfs:
    df_long = df.melt(id_vars=[df.columns[0]], var_name="ABC", value_name="Value")
    final_dfs.append(df_long)

result = pd.concat(final_dfs, ignore_index=True)
grouped_result = result.groupby([result.columns[0], "ABC"], as_index=False).agg({"Value": "sum"})
pivoted_result = grouped_result.pivot(index=grouped_result.columns[0], columns="ABC", values="Value").reset_index()

print(all(pivoted_result == test)) #
