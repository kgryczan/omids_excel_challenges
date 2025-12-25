import pandas as pd
import numpy as np

path = "300-399/345/CH-345 Pattern Recongnition.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=2, nrows=6)
test = pd.read_excel(path, usecols="C", skiprows=2, nrows=6)

input["Count"] = input["Pattern"].apply(
    lambda x: sum(a != b for a, b in zip(x, x[1:]))
)
