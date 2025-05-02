import pandas as pd
import numpy as np
import re

input1 = pd.read_excel("CH-040 Cross Selling.xlsx", sheet_name="Sheet1", skiprows=1, usecols="B:F")
input2 = pd.read_excel("CH-040 Cross Selling.xlsx", sheet_name="Sheet1", skiprows=1, usecols="H:H", names=["Scenario"], nrows=5)
test = pd.read_excel("CH-040 Cross Selling.xlsx", sheet_name="Sheet1", skiprows=1, usecols="K:L", nrows=5)
test = test.sort_values(by=["Customers' Cart"]).reset_index(drop=True)

r1 = input1.groupby('Invoice ID')['Product'].apply(lambda x: list(x.unique())).reset_index(name="products")
r1["products_string"] = r1["products"].apply(lambda x: ",".join(x))

scen_products = input2.copy()
scen_products["Scenario_list"] = scen_products["Scenario"].apply(lambda x: re.split(",", x))

r2 = pd.DataFrame(np.array(np.meshgrid(r1["products_string"], scen_products["Scenario_list"])).T.reshape(-1, 2), columns=["prod", "scen"])
r2 = r2.merge(r1, left_on="prod", right_on="products_string", how="left").drop(columns=["products"])
r2["prod"] = r2["prod"].str.split(",")
r2["is_present"] = r2.apply(lambda x: all(elem in x["prod"] for elem in x["scen"]), axis=1)
r2 = r2[r2["is_present"]].reset_index(drop=True)
r2["diff"] = r2.apply(lambda x: list(set(x["prod"]) - set(x["scen"])), axis=1)
r2 = r2.drop(columns=["prod", "products_string", "is_present"]).reset_index(drop=True)
r2["scen"] = r2["scen"].apply(lambda x: ",".join(x))
r2 = r2.explode("diff").dropna().reset_index(drop=True)
r2 = r2.sort_values(by=["scen", "diff"]).drop_duplicates().reset_index(drop=True)
r2 = r2.groupby(["scen", "diff"]).size().reset_index(name="count")
r2 = r2.sort_values(by=["count"], ascending=False).groupby("scen").head(1).reset_index(drop=True)
r2 = r2[["scen", "diff"]].sort_values(by=["scen"]).reset_index(drop=True)
r2.columns = test.columns

print(r2.equals(test))  # True
