import itertools
import pandas as pd

path = "CH-003.xlsx"
input_data = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="H:I", skiprows=1, nrows=32)

rows = []
ids = input_data["ID"].tolist()
costs = dict(zip(input_data["ID"], input_data["value (cost)"]))
for r in range(1, len(ids) + 1):
    for combo in itertools.combinations(ids, r):
        rows.append({
            "ID Combination": ",".join(combo),
            "Total value (cost)": sum(costs[i] for i in combo),
        })

result = pd.DataFrame(rows)
print(result.equals(test))
