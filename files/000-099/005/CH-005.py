import numpy as np
import pandas as pd

path = "CH-005.xlsx"
input_data = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=20)
test = pd.read_excel(path, usecols="I:L", skiprows=1, nrows=4).fillna(0).astype(int).to_numpy()

prod = (
    input_data.assign(value=1)
    .drop(columns=["Quantity"])
    .pivot_table(index="Invoice Num", columns="Product", values="value", fill_value=0, aggfunc="first")
)
cooc = prod.to_numpy().T @ prod.to_numpy()
np.fill_diagonal(cooc, 0)

print(np.array_equal(cooc, test))
