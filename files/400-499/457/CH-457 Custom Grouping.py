import pandas as pd

path = "400-499/457/CH-457 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:F", skiprows=2, nrows=12)
test = pd.read_excel(path, usecols="H:J", skiprows=2, nrows=7)

data = input.assign(
    PRODUCTS=input.iloc[:, 1:4].apply(lambda x: ",".join(sorted(x.dropna())), axis=1)
).sort_values("Date")
data["group"] = (
    (data.PRODUCTS != data.PRODUCTS.shift()) | data.Date.diff().dt.days.ne(1)
).cumsum()

result = data.groupby("group", sort=False).agg(
    PRODUCTS=("PRODUCTS", "first"),
    QUANTITY=("Quantity", "sum"),
    start=("Date", "min"),
    end=("Date", "max"),
)
result["dates"] = result.apply(
    lambda r: (
        f"{r.start.day}/{r.start.month}/{r.start.year}"
        if r.start == r.end
        else f"{r.start.day}/{r.start.month}/{r.start.year}-{r.end.day}/{r.end.month}/{r.end.year}"
    ),
    axis=1,
)
result = result.reset_index(drop=True)[["PRODUCTS", "QUANTITY", "dates"]]
print(result.equals(test))
# Some sorting discrepancies
