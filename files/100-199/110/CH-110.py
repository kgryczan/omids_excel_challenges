import pandas as pd
import itertools
import re

path = "CH-110-Reconciliation .xlsx"
input1 = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=6)
input2 = pd.read_excel(path, usecols="F:H", skiprows=1, nrows=8)
input2.columns = ['ID', 'Date', 'Value']
test = pd.read_excel(path, usecols="J:J", skiprows=1, nrows=7)

def generate_combinations_with_cumsum(financial_values, financial_ids):
    n = len(financial_values)
    all_combinations = []
    for i in range(1, n+1):
        comb = itertools.combinations(range(n), i)
        for subset_idx in comb:
            subset_vals = [financial_values[j] for j in subset_idx]
            subset_ids = [str(financial_ids[j]) for j in subset_idx]
            cumsum_vals = sum(subset_vals)
            all_combinations.append({
                'IDs': ', '.join(subset_ids),
                'Values': ', '.join(map(str, map(float, subset_vals))),
                'CumSum': cumsum_vals
            })
    return pd.DataFrame(all_combinations)

financial_combinations = generate_combinations_with_cumsum(input2['Value'], input2['ID'])
bank_combinations = generate_combinations_with_cumsum(input1['Value'], input1['ID'])

def match_combinations(target_data, combination_data, match_col):
    matched = {}
    for i in range(len(target_data)):
        target_value = target_data['Value'][i]
        target_id = target_data['ID'][i]
        matching_combinations = combination_data[combination_data[match_col] == target_value]
        
        if len(matching_combinations) > 0:
            matched[target_id] = matching_combinations.to_dict('records')   
    flattened_data = []
    for target_id, combinations in matched.items():
        for combination in combinations:
            flattened_data.append({
                'Target ID': target_id,
                'Combination IDs': combination['IDs'],
                'Combination Values': combination['Values'],
                'Cumulative Sum': combination['CumSum']
            })
    return pd.DataFrame(flattened_data)

forward_matches = match_combinations(input1, financial_combinations, "CumSum")
backward_matches = match_combinations(input2, bank_combinations, "CumSum")

all_matches = pd.concat([forward_matches, backward_matches], ignore_index=True)

all_matches['bank_id'] = all_matches.apply(lambda x: x['Target ID'] if 'B' in x['Target ID'] else x['Combination IDs'], axis=1)
all_matches['fin_id'] = all_matches.apply(lambda x: x['Target ID'] if 'F' in x['Target ID'] else x['Combination IDs'], axis=1)
all_matches['value'] = all_matches['Cumulative Sum']

all1 = all_matches[['bank_id', 'fin_id', 'value']].drop_duplicates()

dfs = []
for i in range(1, len(all1)+1):
    for subset in itertools.combinations(all1.iterrows(), i):
        df = pd.DataFrame([x[1] for x in subset])
        dfs.append(df)

dfs = [df for df in dfs if df['value'].sum() == input1["Value"].sum()]

for i, df in enumerate(dfs):
    df['df_index'] = i

dfs = pd.concat(dfs, ignore_index=True)

all_bank_ids = ["B1", "B2", "B3", "B4", "B5"]
all_fin_ids = ["F1", "F2", "F3", "F4", "F5", "F6", "F7"]
df_grouped = dfs.groupby('df_index').agg({'bank_id': lambda x: ', '.join(x), 'fin_id': lambda x: ', '.join(x)})
df_grouped['bank_id'] = df_grouped['bank_id'].apply(lambda x: re.findall(r'B\d', x))
df_grouped['fin_id'] = df_grouped['fin_id'].apply(lambda x: re.findall(r'F\d', x))

def check_coverage(row):
    bank_ids = row['bank_id']
    fin_ids = row['fin_id']
    return len(bank_ids) == len(all_bank_ids) and len(fin_ids) == len(all_fin_ids) and set(bank_ids) == set(all_bank_ids) and set(fin_ids) == set(all_fin_ids)

df_grouped['coverage'] = df_grouped.apply(check_coverage, axis=1)
df_indexes = df_grouped[df_grouped['coverage']].index

dfs = dfs[dfs['df_index'].isin(df_indexes)]
dfs['bank_id'] = dfs['bank_id'].str.replace(', ', '+')
dfs['fin_id'] = dfs['fin_id'].str.replace(', ', '+')
dfs['bank_id'] = dfs['bank_id'] + "=" + dfs['fin_id'] 
dfs = dfs.groupby('df_index').agg({'bank_id': lambda x: ', '.join(sorted(x))}).reset_index(drop=True)

print(dfs['bank_id'].isin(test['Senarios']).all()) # True
