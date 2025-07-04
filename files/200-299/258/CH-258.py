import pandas as pd
import json

path = "200-299/258/CH-258 Column Splitting.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=5)
test = pd.read_excel(path, usecols="D:H", skiprows=1, nrows=5)

result = (
    pd.DataFrame(
        input['Text']
        .str.replace(r"([a-zA-Z0-9\.]+)", r'"\1"', regex=True)
        .map(json.loads)
        .tolist()
    )
    .assign(age=lambda x: x['age'].astype(float))
)

print(result.equals(test))
