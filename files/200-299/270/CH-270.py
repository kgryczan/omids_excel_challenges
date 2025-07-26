from sympy import symbols, Eq, solve, sympify
import pandas as pd

path = "200-299/270/CH-270 Solving equations.xlsx"
input = pd.read_excel(path, usecols="B:C", nrows=5, skiprows=1)
test = pd.read_excel(path, usecols="E:F", nrows=5, skiprows=1)

X = symbols('X')
eqs = input.iloc[:, 1]
solutions = [
    [round(float(sol.evalf()), 4) for sol in solve(sympify(eq.replace('=', '-(') + ')'), X)]
    for eq in eqs
]

input['Solution'] = solutions
print(input)

