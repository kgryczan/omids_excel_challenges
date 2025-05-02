import pandas as pd

input = pd.read_excel("CH-027 Extract Numbers.xlsx", sheet_name="Sheet1", usecols="B", nrows = 13)
test = pd.read_excel("CH-027 Extract Numbers.xlsx", sheet_name="Sheet1", usecols="E:H", nrows = 13)
test.columns = ['Number_1', 'Number_2', 'Number_3', 'Number_4']

extracted_numbers = input["Question Tables"].str.extractall(r'\((\d+)\)').groupby(level=0)[0].apply(list)
extracted_numbers = extracted_numbers.apply(pd.Series)
extracted_numbers.columns = [f"Number_{i+1}" for i in extracted_numbers.columns]

result = pd.concat([input, extracted_numbers], axis=1)
result = result.iloc[:, 1:]
result = result.astype(float)

print(result.equals(test)) # True