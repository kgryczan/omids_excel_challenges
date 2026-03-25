import pandas as pd

input_data = pd.read_excel("CH-012.xlsx", usecols="B:G", skiprows=2, nrows=6, header=None)
result = input_data.divide(input_data.sum(axis=0), axis=1)

print((result * 100).round(0))
# The R source notes that some workbook comparison cells are incorrect.
