import pandas as pd
import matplotlib.pyplot as plt

path = "200-299/288/CH-288 Transforming.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=9)
test = pd.read_excel(path, usecols="G:H", skiprows=1, nrows=5).rename(columns=lambda col: col.replace('.1', ''))

input['Product'] = input.apply(lambda row: row['Product'] if row['Price'] >= 10 else 'Other', axis=1)
result = input.groupby('Product', as_index=False)['Price'].sum()
result = result.sort_values('Price', ascending=False).reset_index(drop=True)
print(result.equals(test))

pie = result.copy()
plt.figure(figsize=(6, 6))
plt.pie(
    pie['Price'],
    labels=pie['Product'],
    autopct='%1.1f%%',
    startangle=90
)
plt.title("Price Distribution by Product")
plt.axis('equal')
plt.show()
