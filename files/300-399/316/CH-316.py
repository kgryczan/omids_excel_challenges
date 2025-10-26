import pandas as pd

path = "300-399/316/CH-316 Convert Text.xlsx"

input = pd.read_excel(path, usecols="B", nrows=6)
test = pd.read_excel(path, usecols="C", nrows=6)

result = input.copy()
result['Question'] = input['Question'].str.swapcase()

print(result.equals(test)) #not all answers provided are correct