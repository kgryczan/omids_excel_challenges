import pandas as pd
import itertools

path = "200-299/260/CH-260 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=9)
test  = pd.read_excel(path, usecols="E:G", skiprows=1, nrows=9)

inp = input.set_index('ID')['Value'].to_dict()

k = 3
group_size = len(inp) // k
target = sum(inp.values()) / k

valid_groups = [
    group for group in itertools.combinations(inp.keys(), group_size)
    if sum(inp[id_] for id_ in group) == target
]

all_partitions = []
used = set()

for groups in itertools.product(valid_groups, repeat=k):
    flat = [id_ for group in groups for id_ in group]
    if len(set(flat)) == len(inp):
        sorted_groups = tuple(sorted(tuple(sorted(g)) for g in groups))
        key = tuple(sorted_groups)
        if key not in used:
            used.add(key)
            all_partitions.append(sorted_groups)

for idx, partition in enumerate(all_partitions, 1):
    print(f"Partition {idx}:")
    for gidx, group in enumerate(partition, 1):
        values = [inp[id_] for id_ in group]
        print(f"  Group {gidx}: IDs {group}, Values {values}, Sum = {sum(values)}")
    print("-" * 40)

# Partition 1:
#   Group 1: IDs (1, 4, 8), Values [4, 11, 3], Sum = 18
#   Group 2: IDs (2, 5, 9), Values [7, 5, 6], Sum = 18
#   Group 3: IDs (3, 6, 7), Values [1, 9, 8], Sum = 18
# ----------------------------------------
# Partition 2:
#   Group 1: IDs (1, 5, 6), Values [4, 5, 9], Sum = 18
#   Group 2: IDs (2, 7, 8), Values [7, 8, 3], Sum = 18
#   Group 3: IDs (3, 4, 9), Values [1, 11, 6], Sum = 18
# ----------------------------------------