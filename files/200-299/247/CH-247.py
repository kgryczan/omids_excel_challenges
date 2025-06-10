from datetime import date, timedelta
import pandas as pd

path = "200-299/247/CH-247 Date Calculation.xlsx"
test = pd.read_excel(path, usecols="B", skiprows=1, nrows=12)

first_mondays = [
    d + timedelta((7 - d.weekday()) % 7)
    for d in [date(2025, m, 1) for m in range(1, 13)]
]
first_mondays = pd.to_datetime(first_mondays)
first_mondays = pd.DataFrame(first_mondays, columns=["Dates"])

print(test.equals(first_mondays))
# True