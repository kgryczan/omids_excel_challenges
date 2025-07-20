from datetime import datetime, timedelta
import pandas as pd

path = "200-299/267/CH-267 Date Calculation.xlsx"
test = pd.read_excel(path, usecols="B", skiprows=1, nrows=13)

format = "%Y/%m/%d"
def calculate_last_sunday_and_monday(year):
    dates = []
    for month in range(1, 13):
        last_day_of_month = datetime(year, month + 1, 1) - timedelta(days=1) if month != 12 else datetime(year, 12, 31)
        last_sunday = last_day_of_month - timedelta(days=(last_day_of_month.weekday() + 1) % 7)
        last_monday = last_sunday - timedelta(days=6)
        dates.append(f"{last_monday.strftime(format)} - {last_sunday.strftime(format)}")
    
    return pd.DataFrame({"Dates": dates})

result = calculate_last_sunday_and_monday(2025)
# May is crossing month boundary, so the last Sunday is in June