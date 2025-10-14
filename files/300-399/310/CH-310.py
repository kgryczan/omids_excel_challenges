import pandas as pd
from itertools import combinations

input = pd.read_excel("300-399/310/CH-310 Numbers Combination.xlsx", usecols="B", nrows=9)
input = input.rename(columns={input.columns[0]: "Question"})
questions = input["Question"].tolist()

combos = list(combinations(questions, 3))
result = pd.DataFrame(combos, columns=["i1", "i2", "i3"])

result = result[(result["i1"] < result["i2"]) & (result["i2"] < result["i3"])]

result["Result"] = result.apply(lambda row: f"{row['i1']},{row['i2']},{row['i3']}", axis=1)
result = result[["Result"]].sort_values("Result").drop_duplicates().reset_index(drop=True)
print(result)