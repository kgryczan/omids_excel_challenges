import pandas as pd

path = "CH-107 Matching Tables.xlsx"

T1 = pd.read_excel(path, usecols="B:C", skiprows=1,  nrows=7, names=["Question ID", "Response"])
T2 = pd.read_excel(path, usecols="E:F", skiprows=1, nrows=7, names=["Question ID", "Response"])
test = pd.read_excel(path, usecols="H:I", skiprows=1, names=["Question ID", "Response"])

T_full = pd.merge(test["Question ID"], T1, on="Question ID", how="outer")
T_full = pd.merge(T_full, T2, on="Question ID", how="outer")
T_full["Number"] = T_full["Question ID"].str.extract("(\d+)").astype(int)
T_full = T_full.sort_values(by="Number", ascending=True).reset_index(drop=True)
T_full["Response"] = T_full["Response_y"].fillna(T_full["Response_x"])
T_full = T_full.drop(columns=["Response_x", "Response_y", "Number"])

print(T_full.equals(test)) # True