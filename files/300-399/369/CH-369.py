import pandas as pd
import numpy as np

path = "300-399/369/CH-369 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:E", skiprows=2, nrows=8)
test = pd.read_excel(path, usecols="H:I", skiprows=2, nrows=2)

n = len(input)
mid = int(np.ceil(n / 2))
g = (
    input
    .assign(rn=lambda d: np.arange(1, n + 1))
    .assign(group=lambda d: np.select(
        [d.rn < mid, d.rn > mid],
        ["Group 1", "Group 2"],
        default="Middle"
    ))
    .groupby("group")["Total Sales"]
    .sum()
)
g1, g2, m = g.get("Group 1", 0), g.get("Group 2", 0), g.get("Middle", 0)

result = pd.DataFrame({
    "IDs": ["Group 1", "Group 2"],
    "Sales": [g1 + (m if g1 < g2 else 0),
              g2 + (m if g2 <= g1 else 0)]
})

print(result.equals(test))
# Output: True