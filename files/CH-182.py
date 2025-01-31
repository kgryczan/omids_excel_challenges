import pandas as pd

path = "CH-182 Indexing Blank cells.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=12, dtype=str)
test = pd.read_excel(path, usecols="F:H", skiprows=1, nrows=12, dtype=str).rename(columns=lambda x: x.split('.')[0])

flat_values = input.values.flatten(order='C')

counter = 1
for i in range(len(flat_values)):
    if pd.isna(flat_values[i]):
        flat_values[i] = f'B{counter}'
        counter += 1

result = pd.DataFrame(flat_values.reshape(input.shape), columns = input.columns)

print(result.equals(test)) # True