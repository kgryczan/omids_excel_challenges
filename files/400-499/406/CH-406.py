import pandas as pd

path = "400-499/406/CH-406 Number Series.xlsx"
input = pd.read_excel(path, usecols="B", nrows=8, skiprows=2)
test = pd.read_excel(path, usecols="D", nrows=8, skiprows=2)

def make_fibonacci():
	cache = {0: 0, 1: 1}
	def f(n):
		n = int(n)
		if n in cache:
			return cache[n]
		cache[n] = f(n - 1) + f(n - 2)
		return cache[n]
	return f
fibonacci = make_fibonacci()
result = input.copy()
result["Fibonacci Number"] = result["n"].apply(lambda x: float(fibonacci(x)))

all(result["Fibonacci Number"] == test["Fibonacci Number"])
# [1] True
