import pandas as pd

path = "CH-081 Compaint grouping.xlsx"

input1 = pd.read_excel(path, skiprows=1, usecols="B:F", nrows= 4)
input2 = pd.read_excel(path, skiprows=1, usecols="H:J")
test = pd.read_excel(path, skiprows=1, usecols="K:K")

result1 = input1.melt(id_vars=["From-To"], var_name="To", value_name="Distance")

result2 = input2.assign(Path=input2["Path"].str.split(",")).explode("Path")
result2["to"] = result2.groupby(["Date","Staff ID"])["Path"].shift(-1)
result2 = result2.dropna()

result = result2.merge(result1, left_on=["Path", "to"], right_on=["From-To", "To"])
result = result.groupby(["Date", "Staff ID"]).agg({"Distance": "sum"}).reset_index()

print(result["Distance"].equals(test["Distance"])) # True