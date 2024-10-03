import pandas as pd

path = "CH-122 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="C:E", skiprows=1, nrows=26)
test = pd.read_excel(path, usecols="G:J", skiprows=1, nrows=15).rename(columns=lambda x: x.replace('.1', ''))

block_size = 5

input['row_id'] = input.index + 1
input['block_id'] = (input['row_id'] - 1) // block_size + 1

result = input.groupby('block_id').apply(
    lambda x: pd.DataFrame({
        'date': [x['Date'].iloc[1]] * (block_size - 2),
        'region': [x['Date'].iloc[0]] * (block_size - 2),
        'fruits': x['Description'].iloc[2:block_size].tolist(),
        'values': x['Qty'].iloc[2:block_size].tolist()
    })
).reset_index(level=1, drop=True)

result = result.sort_values(by=['date', 'block_id', 'values'], ascending=[True, True, False]).reset_index(drop=True)
result = result.assign(date=pd.to_datetime(result['date']), values=result['values'].astype("int64"))

result.columns = test.columns

print(result.equals(test))
# True