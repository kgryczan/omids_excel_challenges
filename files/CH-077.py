import pandas as pd
import numpy as np

path = "CH-77 Character-Based Rhombus.xlsx"
test = pd.read_excel(path, header=None, usecols="C:Q", skiprows=1, nrows=16)
test = test.fillna("_")
test = test.apply(lambda x: "".join(x), axis=1)

def draw_rhombus(diag):
    if diag % 2 == 0:
        raise ValueError("diag must be an odd number")
    
    rhombus = np.full((diag, diag), "_")
    seq = np.arange(1, diag+1, 2)
    rev_seq = np.flip(seq)[1:]
    seq = np.concatenate((seq, rev_seq))
    
    for i in range(diag):
        rhombus[i, diag//2-seq[i]//2:diag//2+seq[i]//2+1] = "*"

    rhombus = pd.DataFrame(rhombus)
    rhombus = rhombus.apply(lambda x: "".join(x), axis=1)

    return rhombus

result = draw_rhombus(15)

print(result.equals(test)) # True