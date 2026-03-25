import pandas as pd

path = "CH-004.xlsx"
input_data = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=16)
test = pd.read_excel(path, usecols="G:H", skiprows=1, nrows=4)

input_data["Mission Date"] = pd.to_datetime(input_data["Mission Date"])

frames = []
for person, g in input_data.groupby("Person"):
    full_dates = pd.DataFrame({"Mission Date": pd.date_range(g["Mission Date"].min(), g["Mission Date"].max(), freq="D")})
    full_dates["Person"] = person
    frames.append(full_dates)
result = pd.concat(frames, ignore_index=True)
result["wday"] = result["Mission Date"].dt.day_name().str[:3]
result = result.merge(input_data.assign(n=1), on=["Person", "Mission Date"], how="left")

for person, idx in result.groupby("Person").groups.items():
    sub = result.loc[idx].copy()
    sub["n"] = sub["n"].where(~((sub["wday"].shift() == "Fri") & (sub["n"].shift() == 1)), 1)
    sub["n"] = sub["n"].where(~((sub["wday"].shift() == "Sat") & (sub["n"].shift() == 1)), 1)
    result.loc[idx, "n"] = sub["n"].values

out = []
for person, g in result.groupby("Person"):
    g = g.copy()
    g["flag"] = g["n"].eq(1)
    g["cons"] = g["flag"].ne(g["flag"].shift(fill_value=False)).cumsum()
    g["n"] = g["n"].fillna(0)
    g["cum1"] = g.groupby("cons")["n"].cumsum()
    out.append({"Person": person, "cum": g["cum1"].sum()})

result2 = pd.DataFrame(out)
print(result2.equals(test))
