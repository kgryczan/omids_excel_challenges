import pandas as pd
path = "CH-210Removing a character.xlsx"

input = pd.read_excel(path, usecols="B", skiprows=1, nrows=5)
test = pd.read_excel(path, usecols="D:E", skiprows=1, nrows=5)

input = input.rename(columns={input.columns[0]: "Text"}).dropna(subset=["Text"])
input = input.assign(rn=range(1, len(input) + 1), characters=input["Text"].apply(list))
input = input.explode("characters").assign(counter=lambda x: x.groupby("characters").cumcount() + 1)
input["rem"] = input["counter"].eq(1).map({True: "Revised Text", False: "Removed chars"})
input = input.groupby(["rn", "rem"])["characters"].apply("".join).unstack().reset_index()
input = input.rename_axis(None, axis=1)[["Revised Text", "Removed chars"]]
print(input)