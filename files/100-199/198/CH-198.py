import pandas as pd
import numpy as np

path = "CH-198 Matrix Calculation.xlsx"

input1 = pd.read_excel(path,usecols="C:D", skiprows=2, nrows=2, header=None).values
input2 = pd.read_excel(path,usecols="C:E", skiprows=5, nrows=3, header=None).values
input3 = pd.read_excel(path,usecols="C:G", skiprows=9, nrows=5, header=None).values
test1  = pd.read_excel(path,usecols="J:K", skiprows=2, nrows=1)
test2  = pd.read_excel(path,usecols="J:L", skiprows=5, nrows=1)
test3  = pd.read_excel(path,usecols="J:N", skiprows=9, nrows=1)

def process(mat):
    result = {}
    for i in range(mat.shape[0]):
        colname = f"Z{i+1}"
        result[colname] = [np.sum(mat[i, :]) + np.sum(mat[:, i])]
    return pd.DataFrame(result)

output1 = process(input1)
print(output1.equals(test1)) # True

output2 = process(input2) 
print(output2.equals(test2)) # True

output3 = process(input3)
print(output3.equals(test3)) # True