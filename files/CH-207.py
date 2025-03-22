import pandas as pd

path = "CH-207 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=17)
test = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=17)

def accumulate_groups(sales, threshold=100, step=50):
    total, group, groups = 0, 1, []
    for x in sales:
        if total + x > threshold:
            group, total = group + 1, x
            threshold += step
        else:
            total += x
        groups.append(group)
    return groups

input["Group"] = accumulate_groups(input["Sales"])

print(input["Group"].equals(test["Group"])) # True
