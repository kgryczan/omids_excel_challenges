import numpy as np
import pandas as pd

path = "300-399/380/CH-380 Matrix Calculation.xlsx"
input_df = pd.read_excel(path, usecols="B:G", skiprows=2, nrows=5, index_col=0)
test = pd.read_excel(path, usecols="J:K", skiprows=2, nrows=5)

weights = 2 ** np.arange(len(input_df))[::-1]

result = (
    (input_df * weights[:, None])
    .sum()
    .sort_values()
    .reset_index(name="score")
    .rename(columns={"index": "Factor"})
    .assign(Rank=lambda df: df.index + 1)
    [["Rank", "Factor"]]
)

print(result.equals(test))
# True