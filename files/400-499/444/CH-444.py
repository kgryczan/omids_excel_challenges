import re
import pandas as pd

path = "400-499/444/CH-444 Replacement.xlsx"
input = pd.read_excel(path, usecols="B:D", nrows=7, skiprows=2)
test = pd.read_excel(path, usecols="F:H", nrows=7, skiprows=2)
test.columns = ["Date", "Product ID", "Total Sales"]


def replace_x(product_id):
    return re.sub(r"(?<!Y)X(?!Y)", "Y", product_id)


result = input.assign(**{"Product ID": input["Product ID"].map(replace_x)})
print(result.equals(test))
# True
