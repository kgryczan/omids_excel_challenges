import pandas as pd

path = "CH-133 Custom Grouping.xlsx"
input_df = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=39)
test_df = pd.read_excel(path, usecols="K:L", skiprows=1, nrows=7)

dates = pd.date_range(start="2024-01-01", end="2024-02-29")
dates_df = pd.DataFrame({'Date': dates})

merged_df = dates_df.merge(input_df, on='Date', how='left')

merged_df['year'] = merged_df['Date'].dt.year
merged_df['month'] = merged_df['Date'].dt.month
merged_df['day'] = merged_df['Date'].dt.day
merged_df['decade_days'] = (merged_df['day'] // 10 + 1).clip(upper=3)

result = merged_df.groupby(['year', 'month', 'decade_days']).agg(
    Total_Sales=('Sales', 'sum'),
    group=('Date', lambda x: f"{x.min().date()} - {x.max().date()}")
).reset_index()

result = result[['group', 'Total_Sales']]
result.columns = ['Group', 'Total Sales']

print(result)
