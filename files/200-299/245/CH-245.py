import pandas as pd

path = "200-299/245/CH-245 Custom Ranking.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=15)
test = pd.read_excel(path, usecols="F:I", skiprows=1, nrows=15).rename(columns=lambda col: col.replace('.1', ''))

g = input.groupby('Group', group_keys=False)
input['group_total'] = g['Score'].transform('sum')
input['group_size'] = g['Score'].transform('size')
input['in_group_rank'] = g['Score'].rank(ascending=False, method='first')

group_totals = input.groupby('Group', as_index=False)['group_total'].first()
group_totals['group_rank'] = group_totals['group_total'].rank(ascending=False, method='first').astype(int)
input = input.merge(group_totals[['Group', 'group_rank']], on='Group')
input['Rank'] = (input['in_group_rank'] + (input['group_rank'] - 1) * input['group_size']).astype(int)
result = input[['ID', 'Group', 'Score', 'Rank']].sort_values('Rank').reset_index(drop=True)

print(result.equals(test)) # True
