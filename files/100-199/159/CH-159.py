import pandas as pd

path = "CH-159 Data Cleaning.xlsx"
input = pd.read_excel(path, usecols="C:I", skiprows=1, nrows=25)
test = pd.read_excel(path, usecols="K:N", skiprows=1, nrows=4)

input = input.melt(id_vars=["Date"], var_name="Sensor", value_name="Temperature").sort_values(by=["Sensor", "Date"])
input['group'] = input.groupby('Sensor')['Temperature'].diff().ne(0).cumsum()
result = input[input.groupby(['Sensor', 'group'])['Temperature'].transform('size') >= 4].groupby('group').agg(
    From=('Date', 'min'),
    TO=('Date', 'max'),
    Sensor=('Sensor', 'first'),
    Temperature=('Temperature', 'first')
).reset_index(drop=True)

print(result.equals(test)) # True
