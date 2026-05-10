import pandas as pd

path = "400-499/409/CH-409 Filter.xlsx"
input = pd.read_excel(path, usecols="B", nrows=8, skiprows=2)
test = pd.read_excel(path, usecols="F", nrows=2, skiprows=2)
result = (
	input.assign(num=input.ID.str.findall(r"\d+"))
	.explode("num")
	.loc[
		lambda d: (d.num.str[0].astype(int) % 2 == 0)
		& (d.num.str[-1].astype(int) % 2 == 1)
	]
)

print(result["ID"].tolist() == test["ID.1"].tolist())
# Output: True