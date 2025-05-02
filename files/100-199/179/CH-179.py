import pandas as pd
import numpy as np

path = "CH-179 Reshape a table.xlsx"
input = pd.read_excel(path, usecols="B:F", skiprows=1, nrows=8).to_numpy()
test = pd.read_excel(path,  usecols="H:J", skiprows=1, nrows=13)

result_df = pd.DataFrame(input.flatten()[~pd.isna(input.flatten())].reshape(-1, 3), columns=["Date", "Product ID", "Quantity"])
result_df["Quantity"] = result_df["Quantity"].astype(np.int64)

print(result_df.equals(test)) # True
