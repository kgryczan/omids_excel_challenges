import pandas as pd

path = "300-399/320/CH-320 Text Cleaning.xlsx"
input = pd.read_excel(path, usecols="B", nrows=7)
test = pd.read_excel(path, usecols="C", nrows=7)

result = pd.DataFrame({
    'Result ID': input.iloc[:, 0].str.extract(r'(\d+)').astype(int).iloc[:, 0]
})

print(result.equals(test)) # True