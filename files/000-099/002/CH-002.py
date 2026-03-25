import pandas as pd

path = "CH-002.xlsx"
input_data = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=18)
test = pd.read_excel(path, usecols="H:J", skiprows=1, nrows=18)

def cumsumbinning(values, limit):
    groups = []
    current_group = 1
    running = 0
    for value in values:
        if running + value > limit and running > 0:
            current_group += 1
            running = 0
        running += value
        groups.append(current_group)
    return groups

result = input_data.copy()
result["Group"] = cumsumbinning(result["Cost"], 120)

print(result["Group"].equals(test["Group"]))
