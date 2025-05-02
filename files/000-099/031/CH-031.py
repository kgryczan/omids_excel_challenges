import pandas as pd

input = pd.read_excel("CH-031 Creat From-To matrix.xlsx", usecols="B:D", skiprows=1, nrows=11)
test = pd.read_excel("CH-031 Creat From-To matrix.xlsx", usecols="F:K", skiprows=1, nrows=5)
test.columns = ["From"] + test.columns[1:].tolist()
test.set_index("From", inplace=True)
test_matrix = test.to_numpy()

t1 = input.pivot(index="From", columns="TO", values="Distance").fillna(0).to_numpy()
t2 = t1.T
t = t1 + t2

print(t==test_matrix) # True for all elements