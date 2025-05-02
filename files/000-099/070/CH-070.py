import pandas as pd

path = "CH-070 coin change problem.xlsx"
test = pd.read_excel(path, usecols = "H:K", skiprows=1, nrows = 12).sort_values(['1$', '2$', '5$', '10$']).reset_index(drop=True)

target = 11
coins = [1, 2, 5, 10]

counts = pd.DataFrame(
    index=pd.MultiIndex.from_product([range(target + 1)] * 4, names=['n1', 'n2', 'n3', 'n4'])
).reset_index()


combinations = counts.assign(
    total=lambda x: x['n1'] * coins[0] + x['n2'] * coins[1] + x['n3'] * coins[2] + x['n4'] * coins[3]
).query('total == @target').drop('total', axis=1).sort_values(['n1', 'n2', 'n3', 'n4']).reset_index(drop=True)
combinations.columns = test.columns 

print(combinations.equals(test)) # True