import pandas as pd

path = "300-399/326/CH-326 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:E", nrows=9, skiprows=1)
test = pd.read_excel(path, usecols="I:J", nrows=3, skiprows=1)

input["min_char"] = input[["From", "To"]].min(axis=1)
input["max_char"] = input[["From", "To"]].max(axis=1)
input["Group"] = (
    input["min_char"] + input["max_char"] + " or " +
    input["max_char"] + input["min_char"]
)
result = (
    input
    .groupby("Group", as_index=False)
    .agg({"Sales": "sum"})
    .rename(columns={"Sales": "Total Sales"})
)

print(result["Total Sales"].equals(test["Total Sales"]))
# values provided were not correct.
# names provided are done using pattern that was not done in provided values