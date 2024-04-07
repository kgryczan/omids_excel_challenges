import pandas as pd

input = pd.read_excel("CH-033 Noise Removing.xlsx", sheet_name="Sheet1",  usecols="B:J", nrows = 16)
test = pd.read_excel("CH-033 Noise Removing.xlsx", sheet_name="Sheet1",  usecols="L:L", nrows = 6)
test.columns = ["respondent"]

r1 = input.drop(columns=['Question ID']).apply(lambda x: x.corr(input.iloc[:, 1:].sum(axis=1) - x)).to_frame().reset_index()
r1.columns = ["respondent", "correlation"]
r1 = r1[r1["correlation"] > 0.3][["respondent"]].reset_index(drop=True)

print(r1.equals(test)) # True
