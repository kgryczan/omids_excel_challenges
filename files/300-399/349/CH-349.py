import pandas as pd
import re

path = "300-399/349/CH-349 Column Splitting.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=2, nrows=5)
test = pd.read_excel(path, usecols="F:K", skiprows=2, nrows=56)

result = (
    input
      .assign( 
          ID=input["ID"].str.replace(
              r"(?<=[A-Za-z])(?=[^A-Za-z])|"
              r"(?<=[0-9])(?=[^0-9])|"
              r"(?<=[^A-Za-z0-9])(?=[A-Za-z0-9])",
              "|",
              regex=True
          )
      ))

split_cols = result["ID"].str.split("|", expand=True)
total_cols = split_cols.shape[1]
split_cols.columns = [f"ID {i+1}" for i in range(total_cols)]

# difference in first row.