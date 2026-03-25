import pandas as pd

input_data = pd.read_excel("CH-025 ABC analysis.xlsx", usecols="B:D", skiprows=1, nrows=13)
test = pd.read_excel("CH-025 ABC analysis.xlsx", usecols="L:M", skiprows=1, nrows=13)

result = (
    input_data.assign(avg_spend_value=lambda df: df["AVG Inventory (unit)"] * df["Value per unit ($)"])
    .sort_values("avg_spend_value", ascending=False)
    .assign(
        total_spend=lambda df: df["avg_spend_value"].sum(),
        cum_spend=lambda df: df["avg_spend_value"].cumsum(),
    )
)
result["cum_percent"] = result["cum_spend"] / result["total_spend"] * 100
result["Class"] = result.apply(
    lambda r: "A" if r["cum_percent"] <= 80 and r.name < len(result) * 0.2
    else ("B" if r["cum_percent"] <= 95 and r.name < len(result) * 0.5 else "C"),
    axis=1,
)
result = result[["Item Code", "Class"]].rename(columns={"Item Code": "Product"})

print(result.equals(test))
