import pandas as pd

input_data = pd.read_excel("CH-020 Transform Higherarchey format.xlsx", usecols="B:C", skiprows=1, nrows=17)
test = pd.read_excel("CH-020 Transform Higherarchey format.xlsx", usecols="E:H", skiprows=1, nrows=9)

result = input_data.assign(
    level=input_data["Code"].astype(str).str.len(),
    first_digit=input_data["Code"].astype(str).str[0],
)
result = result.pivot(index=["Code", "first_digit"], columns="level", values="Description").reset_index()
result = result.sort_values(["first_digit", "Code"])
result[["1", "2", "3"]] = result.groupby("first_digit")[["1", "2", "3"]].ffill()
result = result.loc[result["Code"].astype(str).str.len() == 3, ["Code", "1", "2", "3"]]
result.columns = ["Code", "Lvel 1", "Lvel 2", "Lvel 3"]

print(result.equals(test))
