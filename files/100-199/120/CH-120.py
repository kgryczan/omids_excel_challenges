import pandas as pd

path = "CH-120 payments Durations.xlsx"
input1 = pd.read_excel(path, usecols="B:D", skiprows=1, nrows= 12)
input2 = pd.read_excel(path, usecols="F:H", skiprows=1, nrows=5).rename(columns=lambda x: x.replace('.1', ''))
test  = pd.read_excel(path, usecols="K:L", skiprows=1, nrows= 12)
test['Duration'] = test['Duration'].replace('NP', '0').astype(int).astype(str)

input1["ID"] = pd.Categorical(input1["ID"], categories=input1["ID"].unique(), ordered=True)
input1 = input1.loc[input1.index.repeat(input1["Cost"])].assign(Value=1).reset_index(drop=True)
input1['rownumber'] = input1["Value"].cumsum()
input1 = input1.drop(columns=['Cost'])

input2["ID"] = pd.Categorical(input2["ID"], categories=input2["ID"].unique(), ordered=True)
input2 = input2.loc[input2.index.repeat(input2["Payment"])].assign(Value=1).reset_index(drop=True)
input2['rownumber'] = input2["Value"].cumsum()
input2 = input2.drop(columns=['Payment'])

all_data = pd.merge(input1, input2, on='rownumber', how='outer').sort_values(by='rownumber').reset_index(drop=True)
all_data['pay_time'] = (all_data['Date_y'] - all_data['Date_x']).dt.days.fillna(0).astype(int)
all_data = all_data.groupby(['ID_x', 'ID_y']).agg({'Value_x': 'sum', 'pay_time': 'first'}).reset_index()
all_data['multiplication'] = all_data['Value_x'] * all_data['pay_time']
all_data = all_data.groupby('ID_x').agg({'multiplication': 'sum', 'Value_x': 'sum'}).reset_index()
all_data['average'] = (all_data['multiplication'] / all_data['Value_x']).fillna(0).astype(int).astype(str)
all_data['ID_x'] = all_data['ID_x'].astype(str)
all_data = all_data.drop(columns=['multiplication', 'Value_x'])

all_data.columns = test.columns

print(all_data.equals(test)) # True