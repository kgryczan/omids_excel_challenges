import pandas as pd

path = "CH-072 Fibonacci sequence .xlsx"
test = pd.read_excel(path, usecols="B").values.tolist()
test = [item for sublist in test for item in sublist]

def fibonacci_memo(n, memo={0: 0, 1: 1}):
    if n not in memo:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

def generate_fibonacci_sequence(N):
    return [fibonacci_memo(i) for i in range(N)]

result = generate_fibonacci_sequence(18)
print(result == test)  # True
