import pandas as pd

path = "CH-92 Missing value.xlsx"
input = pd.read_excel(path, usecols="C:F", skiprows= 1, header=None).values
test = pd.read_excel(path, usecols= "K:N", skiprows= 1, header=None).values

def replace_values(x):
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            if x[i, j] == "D":
                x[i, j] = x[i+1, j]
            elif x[i, j] == "U":
                x[i, j] = x[i-1, j]
            elif x[i, j] == "R":
                x[i, j] = x[i, j+1]
            elif x[i, j] == "L":
                x[i, j] = x[i, j-1]
    return x

result = replace_values(input)

print((result == test).all()) # True
