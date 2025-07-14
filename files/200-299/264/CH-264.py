import pandas as pd

path = "200-299/264/CH-264 Extract from Text.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=5)

def extract_substrings(x):
    n = len(x)
    return [x[i:j] for i in range(n) for j in range(i+1, n+1)]

df = input.assign(substrings=input['Text'].apply(extract_substrings)).explode('substrings')
df['len'] = df['substrings'].str.len()
df['n'] = df.groupby(['Text', 'substrings'])['substrings'].transform('count')
filtered = df[df['n'] > 1]
max_len = filtered.groupby('Text')['len'].transform('max')
result = filtered[filtered['len'] == max_len][['Text', 'substrings']].drop_duplicates().rename(columns={'substrings': 'Pattern'})

print(result)
