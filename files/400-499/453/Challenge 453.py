import pandas as pd

path = "400-499/453/CH-453 Number Puzzles - Disarium Number.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=2)
test = pd.read_excel(path, usecols="D", skiprows=2)


def is_disarium(number):
    return (
        sum(int(digit) ** place for place, digit in enumerate(str(number), 1)) == number
    )


numbers = [number for number in range(100, 10_000) if is_disarium(number)][: len(input)]
result = pd.DataFrame({test.columns[0]: numbers})
print(result.equals(test))
