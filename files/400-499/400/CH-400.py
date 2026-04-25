import pandas as pd
import numpy as np
import string

path = "400-499/400/CH-400 Rook Polynomial.xlsx"
input = pd.read_excel(path, usecols="B:J", nrows=9, skiprows=2)
test = pd.read_excel(path, usecols="L", nrows=6, skiprows=2)

input.index = input.iloc[:, 0]
input = input.iloc[:, 1:]
rows = (np.where(input.notna().any(axis=1))[0] + 1).tolist()
cols = (np.where(input.notna().any(axis=0))[0] + 1).tolist()
rows = [input.index[i - 1] for i in rows]
cols = [input.columns[i - 1] for i in cols]
unused_rows = [row for row in input.index if row not in rows][::-1]
unused_cols = [col for col in input.columns if col not in cols]
unused_df = pd.DataFrame(list(zip(unused_rows, unused_cols)), columns=["Unused Rows", "Unused Cols"])
unused_df["Unused"] = unused_df["Unused Cols"] + unused_df["Unused Rows"].astype(str) 
unused_df['Unused'].equals(test['Locations'])
# True