import pandas as pd

path = "400-499/423/CH-423 Number Puzzles - Happy Number.xlsx"
test = pd.read_excel(path, usecols="C", skiprows=2, nrows=8)

def digit_square_sum(n):
	return sum(int(ch) ** 2 for ch in str(n))
def reduce_to_digit(n):
	while n >= 10:
		n = digit_square_sum(n)
	return n
df = (
	pd.DataFrame({"result": range(1_000_001, 1_001_001)})
	.assign(reduced=lambda x: x["result"].map(reduce_to_digit))
	.loc[lambda x: x["reduced"].isin([1, 7])]
	.head(7)
)
