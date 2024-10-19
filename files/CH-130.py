import pandas as pd

path = "CH-130 FIFO.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=11)
test = pd.read_excel(path, usecols="F:I", skiprows=1, nrows=9).rename(columns=lambda x: x.replace('.1', ''))

i_data = input[input['Tyoe'].str.startswith('I')].copy()
i_data = i_data.loc[i_data.index.repeat(i_data['Quantity'])].assign(In=1, rn=lambda x: range(1, len(x) + 1)).reset_index(drop=True)

o_data = input[input['Tyoe'].str.startswith('O')].copy()
o_data = o_data.loc[o_data.index.repeat(o_data['Quantity'])].assign(Out=1, rn=lambda x: range(1, len(x) + 1)).reset_index(drop=True)

all_data = pd.merge(i_data, o_data, on='rn', how='outer').dropna().sort_values(by='rn').reset_index(drop=True)
all_data = all_data.groupby(['Date_x', 'Date_y', 'Tyoe_x', 'Tyoe_y'], as_index=False)['In'].sum()
all_data["Output"] = all_data['Tyoe_y'].str[-1]

all_data = all_data.drop(columns=['Tyoe_x', 'Tyoe_y']).reindex(columns=['Output', 'Date_y', 'Date_x', 'In'])
all_data.columns = test.columns

print(all_data.equals(test)) # True