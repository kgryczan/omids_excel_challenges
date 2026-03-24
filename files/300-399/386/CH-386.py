import numpy as np
import pandas as pd

path = "300-399/386/CH-386 Index.xlsx"
input = pd.read_excel(path, usecols="B:E", skiprows=2, nrows=8)
test = pd.read_excel(path, usecols="G:K", skiprows=2, nrows=8).rename(
    columns=lambda c: __import__("re").sub(r"\.\d+$", "", c)
)

result = input.copy()
first_purchase = result.groupby(["Customer", "Product"]).cumcount() == 0
index_values = np.where(first_purchase, "*", None)
result["Index"] = pd.Series(index_values, dtype="object")

print(result.equals(test))
## Output: True
