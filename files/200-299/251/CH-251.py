import pandas as pd
import numpy as np
from openpyxl import load_workbook
from datetime import datetime

path = "200-299/251/CH-251 Table Transformation.xlsx"
input_df = pd.read_excel(path, header=None, usecols="B:D", skiprows=2, nrows=14)
input_matrix = input_df.values
test = pd.read_excel(path, usecols="F:H", skiprows=1, nrows=7)

flat = input_matrix.flatten()
df = pd.DataFrame({'Value': flat})
df['Group'] = df['Value'].apply(lambda x: isinstance(x, (datetime, np.datetime64))).cumsum()
df['Field'] = df.groupby('Group').cumcount().map({0: 'Date', 1: 'Product', 2: 'Quantity'})
df = df.dropna().pivot(index='Group', columns='Field', values='Value').reset_index(drop=True)
df['Quantity'] = df['Quantity'].astype(int)
df['Date'] = pd.to_datetime(df['Date'])

print(df.equals(test)) #True