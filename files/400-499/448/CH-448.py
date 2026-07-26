import math
import pandas as pd

path = "400-499/448/CH-448 Number Puzzles - Spy Number.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=2, nrows=7)
test = pd.read_excel(path, usecols="D", skiprows=2, nrows=7)


def is_spy(number):
    digits = [int(digit) for digit in str(number)]
    return sum(digits) == math.prod(digits)


def nearest_spy(number):
    for distance in range(number):
        for candidate in (number - distance, number + distance):
            if candidate > 0 and is_spy(candidate):
                return candidate


result = input.assign(nearest_spy=input["Number"].map(nearest_spy))
result = result.rename(columns={"nearest_spy": "Nearest Spy Number"})
# Wrong answer provides
