import pandas as pd

path = "200-299/268/CH-268 Custom Grouping.xlsx"
df = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=15)
df_test = pd.read_excel(path, usecols="F:H", skiprows=1, nrows=15)

conf = [["A101", "A105"], ["B01", "B03"]]

def mut_grp(x, conf):
    grp, seen, out = 1, set(), []
    for id in x:
        if any(set(c) <= seen | {id} for c in conf):
            grp += 1
            seen = {id}
        else:
            seen.add(id)
        out.append(grp)
    return out

df['Group'] = mut_grp(df['ID'], conf)
print(df['Group'].equals(df_test['Group'])) # True