import pandas as pd
path = "200-299/257/CH-257 Date Calculation.xlsx"
test = pd.read_excel(path, usecols="B", skiprows=1, nrows=12)

result = pd.DataFrame({
    "Result": [
        (d - pd.Timedelta(days=d.weekday() % 7)).to_datetime64()
        for d in pd.date_range("2025-01-31", "2025-12-31", freq="ME")
    ]
})

print(result["Result"].equals(test["Dates"])) # True
