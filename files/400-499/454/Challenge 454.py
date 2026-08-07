import re
import pandas as pd

path = "400-499/454/CH-454 Replacement.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=2, nrows=6)
test = pd.read_excel(path, usecols="F:H", skiprows=2, nrows=6)
test.columns = input.columns


def replace_x(product):
    return re.sub(
        r"XXXX|XX", lambda match: "XX" if len(match[0]) == 4 else "X", product
    )


result = input.assign(**{"Product ID": input["Product ID"].map(replace_x)})
print(result.equals(test))
