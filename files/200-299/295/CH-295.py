import pandas as pd
input = pd.read_excel("200-299/295/CH-295 Text Matching.xlsx", usecols="B", skiprows=1, nrows=8)

ids = input['ID'].astype(str).tolist()
def subs(s): return [s[i:j] for i in range(len(s)) for j in range(i+3, len(s)+1)]
result = pd.DataFrame([
    {'ID 1': a, 'ID 2': b, 'substrings': sub}
    for i, a in enumerate(ids) for j, b in enumerate(ids)
    if a != b and a < b
    for sub in subs(a) if sub in b
])

print(result)

# r2: distinct id1/id2 pairs where a substring match exists
r2 = result[['ID 1', 'ID 2']].drop_duplicates().reset_index(drop=True)
print(r2)

#          ID 1      ID 2 substrings
# 0    MX-21551    MX-21F        MX-
# 1    MX-21551    MX-21F       MX-2
# 2    MX-21551    MX-21F      MX-21
# 3    MX-21551    MX-21F        X-2
# 4    MX-21551    MX-21F       X-21
# 5    MX-21551    MX-21F        -21
# 6    MX-21551  MX-M5512        MX-
# 7    MX-21551  MX-M5512        551
# 8      MX-21F  MX-M5512        MX-
# 9   BN-8213F2    RF_821        821
# 10     MA-210  MX-21551        -21
# 11     MA-210    MX-21F        -21
# 12     FF-512  MX-M5512        512

# r2: distinct id1/id2 pairs where a substring match exists
r2 = result[['ID 1', 'ID 2']].drop_duplicates().reset_index(drop=True)
print(r2)

#          ID 1      ID 2
# 0    MX-21551    MX-21F
# 1    MX-21551  MX-M5512
# 2      MX-21F  MX-M5512
# 3   BN-8213F2    RF_821
# 4     MA-210   MX-21551
# 5     MA-210     MX-21F
# 6     FF-512   MX-M5512

