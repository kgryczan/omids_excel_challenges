import pandas as pd

path = "400-499/447/CH-447 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:D", nrows=12, skiprows=2)
test = pd.read_excel(path, usecols="F:H", nrows=7, skiprows=2)

result = (
    input.assign(
        products=lambda x: x["Products"]
        .str.split(",")
        .apply(lambda v: ",".join(sorted(v)))
    )
    .assign(cons=lambda x: x["products"].ne(x["products"].shift()).cumsum())
    .groupby(["products", "cons"], as_index=False)
    .agg(
        PRODUCTS=("products", "first"),
        **{
            "TOTAL QUANTITY": ("Quantity", "sum"),
            "Date_min": ("Date", "min"),
            "Date_max": ("Date", "max"),
            "n": ("Date", "size"),
        }
    )
    .assign(
        DATES=lambda x: x["Date_min"]
        .astype(str)
        .where(
            x["n"].eq(1), x["Date_min"].astype(str) + "-" + x["Date_max"].astype(str)
        )
    )[["PRODUCTS", "TOTAL QUANTITY", "DATES"]]
)
