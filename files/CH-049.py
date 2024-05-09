import pandas as pd

input = pd.read_excel("CH-049 Assignment Problem Part 1.xlsx", usecols="C:F", skiprows=1).values
test = pd.read_excel("CH-049 Assignment Problem Part 1.xlsx", usecols="P:S", skiprows=1).values

input = [[val - min(row) for val in row] for row in input]
input = list(map(list, zip(*input)))
input = [[val - min(row) for val in row] for row in input]
input = list(map(list, zip(*input)))

print(input == test)    # True