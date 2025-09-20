import pandas as pd

path = "200-299/298/CH-298 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=3)
test = pd.read_excel(path, usecols="E:F", skiprows=1, nrows=25)

dates = input["Date"].str.extractall(r"(\d{1,2}/\d{1,2}/\d{4})")[0].unstack()
input['start'] = dates[0]
input['end'] = dates[1]
input['date_seq'] = input.apply(lambda row: pd.date_range(row['start'], row['end']).strftime('%Y-%m-%d').tolist(), axis=1)
input['seq_length'] = input.apply(lambda row: len(pd.date_range(row['start'], row['end'])), axis=1)
input['Daily Sale'] = input['Total Sales'] / input['seq_length']
input = input[['date_seq', 'Daily Sale']]
result = input.explode('date_seq').reset_index(drop=True)

# result is not equal because of mistake in data provided
# expected = pd.DataFrame({
