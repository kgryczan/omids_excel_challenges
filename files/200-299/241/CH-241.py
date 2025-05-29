import pandas as pd

path = "200-299/241/CH-241 Moving Average.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=18)
test = pd.read_excel(path, usecols="G", skiprows=1, nrows=18)
test['Moving Average'] = pd.to_numeric(test['Moving Average'], errors='coerce')

def moving_average(sales):
    result = []
    for i in range(len(sales)):
        non_zero = [x for x in sales[:i] if x != 0]
        if len(non_zero) >= 2:
            result.append(sum(non_zero[-2:]) / 2)
        else:
            result.append(float('nan'))
    return result

input['Moving Average'] = moving_average(input['Sales'])

print(input['Moving Average'].equals(test['Moving Average']))
