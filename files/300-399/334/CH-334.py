import pandas as pd

input = pd.read_excel("300-399/334/CH-334 Custom Condition.xlsx", usecols="B:D", skiprows=1, nrows=10)
test = pd.read_excel("300-399/334/CH-334 Custom Condition.xlsx", usecols="H", skiprows=1, nrows=3).iloc[:, 0].tolist()
result = (
    input.sort_values("Date")
    .groupby("Issue ID", as_index=False)
    .tail(1)
    .query('Status != "Close"')["Issue ID"]
    .tolist()
)

# Solution provided not correct.