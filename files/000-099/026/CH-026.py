import pandas as pd
from itertools import product
import itertools

# Read Excel files
input = pd.read_excel("CH-026 Calculate the spending time.xlsx", usecols="B:E", skiprows=1, nrows=17)
test = pd.read_excel("CH-026 Calculate the spending time.xlsx", usecols="G:L", skiprows=1, nrows=5)
test = test.round(2)  # Round numeric columns to 2 decimal places

# Process input
input[['hours', 'minutes', 'seconds']] = input['Duration'].astype('str').str.split(':', expand=True)
input['Duration'] = pd.to_numeric(input['hours']) * 3600 + pd.to_numeric(input['minutes']) * 60
input = input.iloc[:, [0, 1, 2, 3]]  # select columns by index

# Combine and sort names to create pairs, then rearrange columns
input['pair'] = input[['Person 1', 'Person 2']].apply(lambda x: '_'.join(sorted(x)), axis=1)
input[['P1', 'P2']] = input['pair'].str.split('_', expand=True)
input = input.groupby('P1').apply(lambda x: x.sort_values('P1')).reset_index(drop=True)
input.drop(columns=['Date'], inplace=True)

pairs = list(product(['A', 'B', 'C', 'D', 'E'], repeat=2))
pairs = pd.DataFrame(pairs, columns=['P1', 'P2'])

r2 = input[["P1", "P2", "Duration"]]
r2 = pairs.merge(r2, how='left', on=['P1', 'P2']).fillna(0)
r2['Duration'] = r2.groupby(['P1', 'P2'])['Duration'].transform('sum')
r2.drop_duplicates(inplace=True)
r2.reset_index(drop=True, inplace=True)

r3 = r2.pivot(index='P1', columns='P2', values='Duration')
r3.rename_axis(index='Month', columns='Interacted With', inplace=True)

r4 = r2.pivot(index='P2', columns='P1', values='Duration')
r4.rename_axis(index='Month', columns='Interacted With', inplace=True)

r5 = r4.add(r3, fill_value=0)
r5 = r5.div(r5.sum(axis=1), axis=0).round(2)
r5 = r5.reset_index().rename_axis(None, axis=1)  

print(r5.equals(test))