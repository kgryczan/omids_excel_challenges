import pandas as pd

input1 = pd.read_excel("CH-013.xlsx", usecols="B", skiprows=1, nrows=12)
patterns = pd.read_excel("CH-013.xlsx", usecols="D:F", skiprows=2, nrows=4, header=None)
test = pd.read_excel("CH-013.xlsx", usecols="I:L", skiprows=1, nrows=5).iloc[:, 1:].fillna(0).astype(int)
test.columns = ["pv", "wind", "bat", "ev"]

regexes = patterns.apply(lambda row: "|".join(row.dropna().astype(str)), axis=1).tolist()
labels = ["pv", "wind", "bat", "ev"]

flags = pd.DataFrame({
    label: input1["Article Titles"].str.contains(regex, regex=True).astype(int)
    for label, regex in zip(labels, regexes)
})
cooc = flags.T.dot(flags)
cooc.index = labels
cooc.columns = labels

print(cooc.equals(test))
