import pandas as pd

path = "CH-016 .xlsx"
input_data = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=14)
test = pd.read_excel(path, usecols="F:I", skiprows=1, nrows=5)

input_data["name"] = (input_data.iloc[:, 0] == "Name").cumsum()
result = (
    input_data.groupby(["name", input_data.columns[0]], as_index=False)[input_data.columns[1]]
    .agg(lambda s: " and ".join(s.astype(str)))
    .pivot(index="name", columns=input_data.columns[0], values=input_data.columns[1])
    .reset_index(drop=True)
)

print(result.equals(test))
