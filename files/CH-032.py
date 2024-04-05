import pandas as pd

input = pd.read_excel("CH-032 Transformation.xlsx", usecols="B:H", skiprows=1, nrows= 14, header=None) 
test  = pd.read_excel("CH-032 Transformation.xlsx", usecols="J:L", skiprows=1, nrows=38)
test.columns = ["Month", "Year", "Sales"]

input.columns = input.iloc[0].astype("str").fillna('') + '' + input.iloc[1].fillna('')
input = input.drop([0,1], axis=0).reset_index(drop=True)
input = input.loc[:, ~input.columns.str.contains('%')]
input = input.melt(id_vars=["Month"], var_name="Year", value_name="Sales")
input["Year"] = input["Year"].str.extract('(\d+)').astype("int")
input["Month"] = input["Month"].astype("int")
input["Sales"] = input["Sales"].astype("int")

print(input == test) # all True