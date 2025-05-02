import pandas as pd
import numpy as np

path = "CH-178 Prime Factors.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="F:G", skiprows=1, nrows=6)

def find_prime_factors(n):
    factors = []
    for divisor in range(2, int(n**0.5) + 1):
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
    if n > 1:
        factors.append(n)
    return "*".join(map(str, factors))

input['prime_factors'] = input.iloc[:, 0].apply(find_prime_factors)

print(all(input["prime_factors"] == test['Result 1'])) # True