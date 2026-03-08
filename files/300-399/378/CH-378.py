import pandas as pd
import re

path = "300-399/378/CH-378 Table Transformation.xlsx"
input_df = pd.read_excel(path, usecols="B", skiprows=2, nrows=9, dtype=str)
test = pd.read_excel(path, usecols="D:F", skiprows=2, nrows=6)

df = (
    input_df["Col1"]
    .str.split(", ")
    .explode()
    .reset_index(drop=True)
    .to_frame()
)
def classify(val):
    if len(val) > 3:
        return "Date"
    elif re.match(r"^[A-Za-z]+$", val):
        return "Product"
    else:
        return "Sale"
df["type"] = df["Col1"].apply(classify)
df["rn"] = df.groupby("type").cumcount()
result = (
    df.pivot(index="rn", columns="type", values="Col1")
    .reset_index(drop=True)
)
result.columns.name = None
result["Sale"] = pd.to_numeric(result["Sale"])

print(result.equals(test))
# Different dates formating. But transformation is correct. 