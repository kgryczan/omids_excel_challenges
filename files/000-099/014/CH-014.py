import pandas as pd

input_data = pd.read_excel("CH-014.xlsx", usecols="B:D", skiprows=1, nrows=132)
test = pd.read_excel("CH-014.xlsx", usecols="K", skiprows=1, nrows=4)

input_data["Date"] = pd.to_datetime(input_data["Date"])
result = (
    input_data.assign(month=input_data["Date"].dt.month)
    .groupby("Product", as_index=False)["month"]
    .nunique()
)
result = result.loc[result["month"] == 12, ["Product"]].rename(columns={"Product": "Products"})

print(result.equals(test))
