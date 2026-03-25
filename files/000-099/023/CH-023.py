import pandas as pd

input1 = pd.read_excel("CH-023 Advance Weighted AVG.xlsx", usecols="B:E", skiprows=1, nrows=17)
input2 = pd.read_excel("CH-023 Advance Weighted AVG.xlsx", usecols="G:J", skiprows=1, nrows=4)
test = pd.read_excel("CH-023 Advance Weighted AVG.xlsx", usecols="L:M", skiprows=1, nrows=4)

prod = input2.melt(id_vars="Month", var_name="Machine Code", value_name="value")
result = (
    input1.groupby(["Month", "Machine Code"], as_index=False)["Weight (KG/Meter)"]
    .mean()
    .rename(columns={"Weight (KG/Meter)": "Avg"})
    .merge(prod, on=["Machine Code", "Month"], how="left")
    .groupby("Month", as_index=False)
    .apply(lambda g: pd.Series({"AVG weight (Kg/Meter)": round((g["Avg"] * g["value"]).sum() / g["value"].sum(), 2)}))
    .reset_index(drop=True)
)

print(result.equals(test))
