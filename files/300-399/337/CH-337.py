import pandas as pd
import numpy as np

excel_path = "300-399/337/CH-337 Rows Grouping.xlsx"
input = pd.read_excel(excel_path, usecols="B:C", skiprows=1, nrows=10)
test = pd.read_excel(excel_path, usecols="G:H", skiprows=1, nrows=5)
test.columns = [col.replace('.1', '') for col in test.columns]

input[["Level1", "Level2"]] = input["Level"].str.split(" ", n=1, expand=True)
grouped = (
    input
    .groupby("Issue ID", as_index=False)
    .agg({
        "Level1": "first",
        "Level2": lambda x: ",".join(x.dropna())
    })
)
grouped["Level"] = (grouped["Level1"] + " " + grouped["Level2"]).str.strip()
result = grouped[["Issue ID", "Level"]]

print(result.equals(test))
# True