import pandas as pd

path = "400-499/415/CH-415 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="B:C", nrows=20, skiprows=2)
test = pd.read_excel(path, usecols="E:H", nrows=5, skiprows=2)

result = (input.assign(
    name=input["COLUMN"].str.extract(r"([A-Za-z]+)")[0].str.upper(),
    id=input["COLUMN"].str.extract(r"(\d+)")[0]
    )
.pivot(index="id", columns="name", values="VALUE")
.reset_index(drop=True)
 .assign(DATE=lambda df: pd.to_datetime(df["DATE"]))
[["DATE", "PRODUCT", "CUSTOMER", "SALES"]])

print(all(result == test))
# True