import pandas as pd

path = "CH-0010.xlsx"
input_data = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=16)
test = pd.read_excel(path, usecols="G:H", skiprows=1, nrows=6)

requirements_map = {"A": 1, "B": 2, "C": 3}

result = input_data.assign(
    requirements=lambda df: df["Material"].map(requirements_map),
    product_available=lambda df: df["Inventory"] // df["requirements"],
)
result = (
    result.groupby("Date", as_index=False)
    .apply(
        lambda g: pd.Series(
            {
                "usage": (g["product_available"].min() * g["requirements"]).sum(),
                "inventory": g["Inventory"].sum(),
            }
        )
    )
    .reset_index(drop=True)
)
result["Efficiency_rate"] = result["usage"] / result["inventory"]

print(result["Efficiency_rate"].equals(test["Efficeincy Rate"]))
