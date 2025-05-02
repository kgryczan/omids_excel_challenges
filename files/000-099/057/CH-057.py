import pandas as pd

input = pd.read_excel("CH-057 Fuzzy Numbers Calculation.xlsx", sheet_name="Sheet1", usecols="B:C", skiprows=1, nrows = 13)
test = pd.read_excel("CH-057 Fuzzy Numbers Calculation.xlsx", sheet_name="Sheet1", usecols="G:H", skiprows=1, nrows = 13)

input[['A1', 'A2', 'A3']] = input['A'].str.split(',', expand=True).astype(int)
input[['B1', 'B2', 'B3']] = input['B'].str.split(',', expand=True).astype(int)

input['A'] = input[['A1', 'A2', 'A3']].values.tolist()
input['B'] = input[['B1', 'B2', 'B3']].values.tolist()

input['A+B'] = input.apply(lambda row: [str(x + y) for x, y in zip(row['A'], row['B'])], axis=1)
input['A-B'] = input.apply(lambda row: [str(x - y) for x, y in zip(row['A'], row['B'][::-1])], axis=1)

result = input[['A+B', 'A-B']]

result['A+B'] = result['A+B'].apply(lambda x: ','.join(x))
result['A-B'] = result['A-B'].apply(lambda x: ','.join(x))

print(result.equals(test)) # True