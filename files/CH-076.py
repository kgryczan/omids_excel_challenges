import pandas as pd

path = "CH-076 Reverse Stepped Tax.xlsx"

input1 = pd.read_excel(path, usecols="B:D", skiprows=1)
input2 = pd.read_excel(path,  usecols="F:G", skiprows=1)
test = pd.read_excel(path, usecols="F:H", skiprows=1)

in1 = input1.copy()
in1["To"] = in1["To"].apply(lambda x: float("inf") if x == "Over" else float(x))
in1["max_tax"] = round((in1["To"] - in1["From"]) * in1["Tax Rate"]).cumsum()

in2 = pd.merge(input2, in1, how="cross")
in2["tax_in_max_thr"] = in2["Tax"] - in2.groupby("Person ID")["max_tax"].shift(1)
in2 = in2[in2["tax_in_max_thr"] > 0]
in2 = in2.groupby("Person ID").apply(lambda x: x[x["tax_in_max_thr"] == x["tax_in_max_thr"].min()])
in2["Income"] = in2["From"] + in2["tax_in_max_thr"] / in2["Tax Rate"]
in2 = in2.reset_index(drop=True)

print(in2["Income"] - test["Income"])

# 0   -1.222222
# 1    1.421053
# 2   -1.076923
# 3    1.052632
# 4   -0.135135
# Discrepancies because of rounding errors