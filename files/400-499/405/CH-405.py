import pandas as pd

path = "400-499/405/CH-405 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="B:C", nrows=5, skiprows=2)
test = pd.read_excel(path, usecols="E:H", nrows=9, skiprows=2)

result = input.set_index(input.columns[0])[input.columns[1]].to_dict()
result = {str(k): str(v).split(" , ") for k, v in result.items() if str(k) != "nan"}
result = pd.DataFrame(result)
result = result.assign(
    DATE=pd.to_datetime(result["DATE"], format="%d/%m/%Y"),
    SALES=pd.to_numeric(result["SALES"]),
)

print(result.equals(test))
# True