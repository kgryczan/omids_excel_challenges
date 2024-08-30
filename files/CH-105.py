import pandas as pd

path = "CH-105 Character Repetition.xlsx"
input = pd.read_excel(path, usecols = "B", skiprows = 1, nrows = 10)
test  = pd.read_excel(path, usecols = "D:E", skiprows = 1, nrows = 6)


result = (
    input
    .assign(Password=lambda df: df['Password'].str.lower())
    .assign(Character=lambda df: df['Password'].str.split(''))
    .explode('Character')
    .groupby('Character', as_index=False)
    .size()
    .rename(columns={'size': 'Repitation'})
    .query("Character != ''")
    .sort_values(by=['Repitation', 'Character'], ascending=[False, True])
    .reset_index(drop=True)
    .head(6)
)

print(result.equals(test))  # True