import pandas as pd
import re
from datetime import datetime

path = "200-299/228/Ch-228 Table Transformation.xlsx"

input = pd.read_excel(path, skiprows=1, usecols="B:H", nrows = 3)
test = pd.read_excel(path, skiprows=7, usecols="F:H", nrows=18)
test.columns = ["Date", "Product", "Price"]
test["Date"] = test["Date"].apply(
    lambda x: datetime.strptime(re.search(r"\d{1,2}/\d{2}/\d{4}", str(x)).group(), "%d/%m/%Y")
    if re.search(r"\d{1,2}/\d{2}/\d{4}", str(x)) else x
)

input_long = input.melt(id_vars=["Product"], var_name="Date", value_name="Price")
input_long["Date"] = input_long["Date"].apply(
    lambda x: datetime.strptime(re.search(r"\d{1,2}/\d{2}/\d{4}", str(x)).group(), "%d/%m/%Y")
    if re.search(r"\d{1,2}/\d{2}/\d{4}", str(x)) else x
)
input_long = input_long.sort_values(by=["Product", "Date"]).fillna(0).reset_index(drop=True)
input_long["Price"] = input_long.groupby("Product")["Price"].cumsum().astype("int64")
input_long = input_long[["Date", "Product", "Price"]]

print(input_long['Price'].equals(test['Price'])) # True