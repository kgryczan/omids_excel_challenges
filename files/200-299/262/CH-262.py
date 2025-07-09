import pandas as pd
import json

path = "200-299/262/CH-262 JSON Structures.xlsx"

input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=3)
test = pd.read_excel(path, usecols="E:G", skiprows=1, nrows=6).rename(columns=lambda c: c.replace('.1', ''))

def extract_sales(cell):
    if not isinstance(cell, str):
        return []
    try:
        obj = json.loads(cell)
        return obj.get('sales', [])
    except json.JSONDecodeError:
        return []

input['sales_list'] = input['Data'].apply(extract_sales)
result = pd.json_normalize(
    input.explode('sales_list').assign(sales=lambda df: df['sales_list'])[['ID', 'sales']]
    .dropna(subset=['sales'])
    .reset_index(drop=True)['sales']
    .apply(lambda x: x if isinstance(x, dict) else {})
).assign(ID=input.explode('sales_list')['ID'].values)[['ID', 'region', 'val']].rename(columns={'region': 'Region', 'val': 'Value'})


print(result.equals(test))