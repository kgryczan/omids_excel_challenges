import pandas as pd

path = "CH-194 Pattern Length.xlsx"
input = pd.read_excel(path, usecols="A:C", skiprows=1, nrows=5)
test = pd.read_excel(path, usecols="G:H", skiprows=1, nrows=5, dtype={'Length': str}).rename(columns=lambda x: x.split('.')[0])

input = input.assign(Pattern=input['Pattern'].str.split(" ")).explode('Pattern').reset_index(drop=True)
input['cn'] = (input.groupby('Date')['Pattern'].transform(lambda x: (x != x.shift()).cumsum()))
input['n'] = input.groupby(['Date', 'cn'])['Pattern'].transform('size')
max_df = input.loc[input.groupby('Date')['n'].idxmax()].copy()
max_df['Length'] = max_df['Pattern'] + max_df['n'].astype(str)
result = max_df[["Date", "Length"]].reset_index(drop=True)

print(result.equals(test)) # True