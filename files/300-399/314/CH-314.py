import pandas as pd

path = "300-399/314/CH-314 Word Pyramid Split.xlsx"
input = pd.read_excel(path, usecols="B", nrows=7)
test = pd.read_excel(path, usecols="C", nrows=7)

input["Result"] = [
    " | ".join([q[:i] for i in range(1, len(q)+1)])
    for q in input.iloc[:, 0]
]

print(input["Result"].equals(test['Result']))  # True