import itertools
import pandas as pd

path = "CH-128 Cartesian Product.xlsx"
test = pd.read_excel(path, usecols = "C")
lets = ["A","B","C","D"]
combs = [''.join(p) for p in itertools.product(lets, repeat=3)]

print(all(combs == test["Result"])) # True