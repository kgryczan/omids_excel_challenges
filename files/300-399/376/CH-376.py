import pandas as pd


path = "300-399/376/CH-376 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=3, nrows=9, header=None)
test = pd.read_excel(path, usecols="E:G", skiprows=2, nrows=6)

v = pd.Series(input.to_numpy().ravel()).dropna()
v = v[v != ""]

df = pd.DataFrame({"val": v})

df["Date"] = df["val"].where(
    df["val"].apply(lambda x: isinstance(x, str) and bool(__import__('re').match(r"\d{1,2}/\d{1,2}/\d{4}", x)))
    | df["val"].apply(lambda x: isinstance(x, pd.Timestamp) or hasattr(x, 'date'))
)
df["Product"] = df["val"].where(df["val"].str.match(r"^[A-Z]$"))
df["Sale"] = pd.to_numeric(df["val"], errors="coerce")

df["Date"] = pd.to_datetime(df["Date"], dayfirst=True).ffill()
df["Product"] = df["Product"].ffill()

result = df[df["Sale"].notna()][["Date", "Product", "Sale"]]
print(result)
# Different dates in some rows