import pandas as pd

path = "300-399/375/CH-375 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=2, nrows=9)
test = pd.read_excel(path, usecols="E:G", skiprows=2, nrows=5)

input_matrix = input.values
input_array = input_matrix.flatten()
input_array = input_array[~pd.isnull(input_array)]
cell_types = len(set([type(cell) for cell in input_array]))
input_array = input_array.reshape(-1, cell_types)
input_df = pd.DataFrame(input_array, columns=["Date", "Product", "Sale"])

print((input_df == test).all().all())
