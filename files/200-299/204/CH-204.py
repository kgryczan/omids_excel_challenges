import pandas as pd
from itertools import accumulate

path = "CH-204 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=17)
test = pd.read_excel(path, usecols="H:J", skiprows=1, nrows=17)

def accumulate_groups(costs):
    groups, acc_sum, acc_count, group = [], 0, 0, 1
    for cost in costs:
        if acc_sum + cost > 150 or acc_count == 3:
            group += 1
            acc_sum, acc_count = cost, 1
        else:
            acc_sum += cost
            acc_count += 1
        groups.append(group)
    return groups

input['Group'] = accumulate_groups(input['Cost'])

print(input)