import pandas as pd
import matplotlib.pyplot as plt

path = "200-299/279/CH-279 Transforming.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=6)
test  = pd.read_excel(path, usecols="G:H", skiprows=1, nrows=12)

input["prev"] = input["Price"].shift()
result = pd.melt(
    input, id_vars="Date", value_vars=["prev", "Price"], value_name="Price_val"
).dropna()[["Date", "Price_val"]].rename(columns={"Price_val": "Price"})
result = result.sort_values("Date").reset_index(drop=True)
print(result)


plt.plot(result["Date"], result["Price"], marker='o')
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Line Plot of Price Over Date")
plt.show()
