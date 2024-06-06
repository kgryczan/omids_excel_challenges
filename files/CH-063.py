import pandas as pd

input = pd.read_excel("CH-063 Custom splitter.xlsx", usecols="B", skiprows=1)
test = pd.read_excel("CH-063 Custom splitter.xlsx", usecols="D:F", skiprows=1)

pattern = r"(\d{4}/\d{1,2}/\d{1,2})([A-Za-z]{1,2})(\d{1,2})"

result = input["Info"].str.extract(pattern)
result.columns = ["Date", "Product", "Quantity"]
result["Quantity"] = pd.to_numeric(result["Quantity"])

print(result.equals(test)) # True