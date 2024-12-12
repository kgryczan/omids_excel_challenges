import pandas as pd
path = "CH-157 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="C", skiprows=1, nrows=15, dtype=str)
test = pd.read_excel(path, usecols="E:G", skiprows=1, nrows=10)

input_matrix = input.values.reshape(-1, 3)
result = pd.DataFrame(input_matrix, columns=["V1", "V2", "V3"])
result = result.assign(V2=result['V2'].str.split(','), V3=result['V3'].str.split(',')).explode(['V2', 'V3'])
result['V1'] = pd.to_datetime(result['V1'], errors='coerce')
result['V3'] = pd.to_numeric(result['V3'], errors='coerce').astype('Int64')
result.reset_index(drop=True, inplace=True)
result.columns = test.columns
print(all(result == test)) # True