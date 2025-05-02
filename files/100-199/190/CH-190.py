import pandas as pd
from word2number import w2n

path = "CH-190 Convert Text to number.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=4)
test = pd.read_excel(path, usecols="D", skiprows=1, nrows=4)

input['Output'] = input.pop('Date').apply(w2n.word_to_num)

print(input.equals(test)) # True