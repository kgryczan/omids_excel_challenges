import pandas as pd

path = "300-399/315/CH-315 Consecutive numbers.xlsx"
numbers = pd.read_excel(path, usecols="B", nrows=14).iloc[:, 0].values

result = pd.DataFrame(
    [(a, b, c) for a, b, c in zip(numbers, numbers[1:], numbers[2:]) if c - a == 2],
    columns=['V1', 'V2', 'V3']
)
result['Result'] = result.apply(lambda r: f"{r.V1}.{r.V2}.{r.V3}", axis=1)

print(result[['Result']])