import pandas as pd

input = pd.read_excel("CH-041 Transformation.xlsx", usecols="B:E", skiprows=1, nrows = 9)
test = pd.read_excel("CH-041 Transformation.xlsx", usecols="G:H", skiprows=1, nrows = 20)

result = input.copy()
# name columns
result.columns = ["Machinary Code", "Col1", "Col2", "Col3"]
result = result.melt(id_vars=["Machinary Code"], var_name="col", value_name="Product Code").dropna(subset=["Product Code"])
result = result.sort_values(by=["Product Code", "col"])
result = result.drop(columns=["col"]).reset_index(drop=True)

print(result.equals(test)) # True