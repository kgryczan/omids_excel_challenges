import pandas as pd
import itertools

path = "CH-90 TSP.xlsx"
input = pd.read_excel(path,  usecols = "B:G", skiprows=1, nrows = 5)
test = pd.read_excel(path, usecols="J:K", skiprows = 1).sort_values(by="Cost").reset_index(drop=True)
\

mid_cities = ["B", "C", "D", "E"]
city_order_perm = itertools.permutations(mid_cities)

city_order = []
for perm in city_order_perm:
    order = ["A"] + list(perm) + ["A"]
    city_order.append("-".join(order))

city_order_df = pd.DataFrame(city_order, columns=["city_order"])
city_order_df["to_sep"] = city_order_df["city_order"].str.split("-")
city_order_df = city_order_df.explode("to_sep")
city_order_df["lead"] = city_order_df["to_sep"].shift(-1)
city_order_df = city_order_df.dropna()

dist = input.melt(id_vars=["From To"], var_name="to", value_name="dist")

result = city_order_df.merge(dist, left_on=["to_sep", "lead"], right_on=["From To", "to"])
result["city_order"] = result["city_order"].str.replace("-", "")
result = result.groupby("city_order").agg(Cost=("dist", "sum")).reset_index()
result = result.sort_values(by="Cost").sort_values(by ="Cost").reset_index(drop=True)

print(result["Cost"].equals(test["Cost"])) # True