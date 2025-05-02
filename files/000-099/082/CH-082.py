import pandas as pd

path = "CH-082 Attendance Date.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=1, nrows = 5)
test = pd.read_excel(path, usecols="F:G", skiprows=1)

result = input.assign(Date=input.apply(lambda row: pd.date_range(row['From'], row['To'], freq='D'), axis=1)) \
    .explode('Date') \
    .groupby('Date') \
    .agg({'Supervisor': lambda x: ', '.join(x)}) \
    .reset_index()
result.rename(columns={'Supervisor': 'Supervisors'}, inplace=True)

print(result.equals(test)) # True   