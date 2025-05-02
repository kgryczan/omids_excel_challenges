import pandas as pd

path = "CH-085 Custome Ranking.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1)
input["Values"] = input["Values"].apply(lambda x: 56 if x == 51 else x)
test = pd.read_excel(path, usecols="F:G", skiprows=1)
test.columns = test.columns.str.replace(".1", "") 

ab50 = input[input["Values"] > 50].sort_values("Values")["Values"].tolist()
be50 = input[input["Values"] < 50].sort_values("Values", ascending=False)["Values"].tolist()

if len(ab50) > len(be50):
    be50 += [None] * (len(ab50) - len(be50))
else:
    ab50 += [None] * (len(be50) - len(ab50))

df = pd.DataFrame({"ab": ab50, "be": be50})
df["nr"] = df.index + 1
df = df.melt(id_vars="nr", value_vars=["ab", "be"], var_name="type", value_name="Values")
df = df.dropna().reset_index(drop=True)
df["t2"] = df["Values"] - 50 > 0
df = df.sort_values(["nr", "t2"], ascending=[True, False]).reset_index(drop=True)
df["Rank"] = df.index + 1
df = df[["Values", "Rank"]].sort_values("Values")

