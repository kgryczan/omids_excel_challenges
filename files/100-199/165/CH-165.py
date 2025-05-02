import pandas as pd

path = "CH-165 Customer Grouping.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=10)
test = pd.read_excel(path, usecols="F:J", skiprows=1, nrows=4).rename(columns=lambda x: x.split('.')[0])

grid = input.set_index(['Month', 'Customer']).unstack(fill_value=0).stack().reset_index()

def get_status(row, first_date):
    if row['Month'] == first_date:
        return "New"
    if row['Quantity'] == 0:
        return "" if row['Month'] < first_date else "Inactive"
    return "Returning" if row['Quantity_lag'] == 0 else "ACTIVE"

grid['Quantity_lag'] = grid.groupby('Customer')['Quantity'].shift(1).fillna(0)
grid['FirstDate'] = grid.groupby('Customer')['Month'].transform(lambda x: x[grid['Quantity'] > 0].min())
grid['status'] = grid.apply(lambda row: get_status(row, row['FirstDate']), axis=1)

grid = grid[(grid['Month'] > 1) & (grid['status'] != "")]
grid = grid.groupby(['Month', 'status'])['Customer'].apply(', '.join).unstack().reset_index()
grid = grid[['Month', 'New', 'ACTIVE', 'Inactive', 'Returning']]
grid.columns.name = None

print(grid.equals(test)) # True