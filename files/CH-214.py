import pandas as pd
import itertools

path = "CH-214Column Splitting.xlsx"
input_data = pd.read_excel(path, usecols="B", skiprows=1, nrows=6, names=["ID"])
test = pd.read_excel(path, usecols="D:F", skiprows=1, nrows=6)

def generate_substrings(s):
    n = len(s)
    substrings = []
    for start in range(n):
        for end in range(start + 1, n + 1):
            substrings.append(s[start:end])
    return substrings

subs = pd.DataFrame({"substring": generate_substrings("1234567890")})
subs = subs[subs["substring"].str.len() > 1]

result = pd.DataFrame(
    itertools.product(input_data["ID"], subs["substring"]),
    columns=["ID", "match"]
)
result = result[result.apply(lambda row: row["match"] in row["ID"], axis=1)]
result["match_length"] = result["match"].str.len()
result = result.sort_values("match_length", ascending=False).drop_duplicates("ID")
result[["before", "after"]] = result.apply(
    lambda row: pd.Series(row["ID"].split(row["match"])), axis=1
)
result = result.sort_values("ID").reset_index(drop=True)
result = result[["before", "match", "after"]]
result["match"] = result["match"].astype("int64")
result.columns = test.columns

print(result.equals(test)) # True