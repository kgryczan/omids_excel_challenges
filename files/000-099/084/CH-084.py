import pandas as pd

path = "CH-84 Normal Distribution.xlsx"

input1 = pd.read_excel(path, usecols="B:L", skiprows=1)
input2 = pd.read_excel(path, usecols="N", skiprows=1, nrows=7)
test = pd.read_excel(path, usecols="O", skiprows=1, nrows=7)
test.columns = test.columns.str.replace('.1', '')

result1 = input1.melt(id_vars=["Z"], var_name="Z1", value_name="prob")
result1["Z_tot"] = result1["Z1"] + result1["Z"]
result1 = result1[["Z_tot", "prob"]]

result2 = pd.DataFrame({"Probability": input2["Probability"]})
result2["Z"] = result2["Probability"].apply(lambda x: result1.loc[(result1["prob"] - x).abs().idxmin(), "Z_tot"])

result2["Z"] = result2["Z"].round(2)
test["Z"] = test["Z"].round(2)

print(result2["Z"].equals(test["Z"]))  # True
