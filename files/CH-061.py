import pandas as pd

input1 = pd.read_excel("CH-061 Sales per customer.xlsx", usecols="B:D", skiprows=1)
input2 = pd.read_excel("CH-061 Sales per customer.xlsx", usecols="F:G", skiprows=1, nrows = 6)
test = pd.read_excel("CH-061 Sales per customer.xlsx", usecols="I:J", skiprows=1, nrows = 8)\
    .sort_values(by="Sales", ascending=False)\
    .reset_index(drop=True)

def find_latest_id(id, changes):
    new_id = changes.loc[changes['OLD ID'] == id, 'New ID'].values
    if len(new_id) == 0:
        return id
    else:
        return find_latest_id(new_id[0], changes)

transactions = input1.copy()
transactions['Customer'] = transactions['Customer ID'].apply(lambda x: find_latest_id(x, input2))
transactions = transactions.groupby('Customer').agg({'Quantity': 'sum'})\
    .reset_index().rename(columns={'Quantity': 'Sales'})\
    .sort_values(by='Sales', ascending=False).reset_index(drop=True)

print(transactions.equals(test)) # True