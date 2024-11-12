import pandas as pd

path = "CH-142 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="B:E", skiprows=1, nrows=16)
test = pd.read_excel(path, usecols="G:J", skiprows=1, nrows=10).rename(columns=lambda x: x.split('.')[0])

ins = input[input['Type'] == 'In'].rename(columns={'Time': 'In'})
outs = input[input['Type'] == 'Out'].rename(columns={'Time': 'Out'})

result = ins.merge(outs, on=['Date', 'ID']).query('In < Out').sort_values(by=['Date', 'ID', 'In'])\
    .drop_duplicates(subset=['Date', 'ID', 'In']).reset_index(drop=True)

unmatched_ins = pd.merge(ins, result, on=['Date', 'ID', 'In'], how='left', indicator=True)
unmatched_ins = unmatched_ins[unmatched_ins['_merge'] == 'left_only'].drop(columns=['_merge'])

unmatched_outs = pd.merge(outs, result, on=['Date', 'ID', 'Out'], how='left', indicator=True)
unmatched_outs = unmatched_outs[unmatched_outs['_merge'] == 'left_only'].drop(columns=['_merge'])

result['In_Out'] = result[['In', 'Out']].max(axis=1)

result = pd.concat([result, unmatched_outs, unmatched_ins])\
    .sort_values(by=['Date', 'ID', 'In_Out']).reset_index(drop=True)
result = result[['Date', 'ID', 'In', 'Out']]

print(result.equals(test)) # True