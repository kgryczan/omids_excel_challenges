import pandas as pd
import polars as pl
import numpy as np

path = "300-399/323/CH-323 Pattern Combinations.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=10)
test = pd.read_excel(path, usecols="E", skiprows=1, nrows=2).values.flatten()

input_pl = pl.from_pandas(input)
n = input_pl.height

group = np.concatenate([np.repeat(i+1, i+1) for i in range(n)])[:n]
input_pl = input_pl.with_columns(pl.Series("group", group))

input_pl = input_pl.with_columns([
    pl.when(pl.col("group") % 2 == 1).then(pl.col("Column 1")).otherwise(pl.col("Column 2")).alias("f_word"),
    pl.when(pl.col("group") % 2 == 0).then(pl.col("Column 1")).otherwise(pl.col("Column 2")).alias("s_word"),
])

f_word = "".join(input_pl["f_word"].to_list())
s_word = "".join(input_pl["s_word"].to_list())

result = np.array([f_word, s_word])

print((result == test).all())  # True