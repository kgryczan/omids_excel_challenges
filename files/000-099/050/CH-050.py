import itertools
import pandas as pd

path = "CH-050 Assignment Problem Part 2.xlsx"
cost = pd.read_excel(path, usecols="B:F", skiprows=1, nrows=5, index_col=0)
test = pd.read_excel(path, usecols="AK:AL", skiprows=1, nrows=5).sort_values("Person").reset_index(drop=True)

tasks = cost.index.tolist()
people = cost.columns.tolist()

best_perm = None
best_cost = None
for perm in itertools.permutations(people):
    total = sum(cost.loc[task, person] for task, person in zip(tasks, perm))
    if best_cost is None or total < best_cost:
        best_cost = total
        best_perm = perm

result = pd.DataFrame({"Tasks": tasks, "Person": list(best_perm)}).sort_values("Person").reset_index(drop=True)
print(result.equals(test))
