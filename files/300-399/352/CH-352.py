import pandas as pd
from itertools import combinations

path = "300-399\\352\\CH-352 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols = "B", nrows = 6, skiprows = 2 ).values.flatten().tolist()
test = pd.read_excel(path, usecols = "F:H", nrows = 10, skiprows = 2)   

df = pd.DataFrame(
    [
        ( i+1, ", ".join(c), ", ".join(sorted(set(input) - set(c))))
        for i, c in enumerate(combinations(input, 3))
        if c[0] == input[0]
    ],
    columns=["Group #", "Group 1", "Group 2"]
)

print(df.equals(test))
# True