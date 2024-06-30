import pandas as pd

path = "CH-75 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="B:E", skiprows=1, nrows=18)
test = pd.read_excel(path, usecols="I:J", skiprows=1, nrows=3)
test["AVG Delivery Time"] = round(test["AVG Delivery Time"], 2)

orders = input[input["Quantity"] > 0].reset_index(drop=True)
deliveries = input[input["Quantity"] < 0].reset_index(drop=True)

together = pd.merge(orders, deliveries, on="Order ID", how="left")
together["Date_y"] = pd.to_datetime(together["Date_y"])
together["Date_x"] = pd.to_datetime(together["Date_x"])
together["Days"] = (together["Date_y"] - together["Date_x"]).dt.days.astype(int)
together["total_quantity"] = together.groupby("Product_x")["Quantity_y"].transform("sum").multiply(-1)

together["avg_delivery_time"] = (together["Days"] * together["Quantity_y"] * -1) / together["total_quantity"]
together = together.groupby("Product_x")["avg_delivery_time"].sum().round(2).reset_index()
together.columns = test.columns

print(together.equals(test)) # True
