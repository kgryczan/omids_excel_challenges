import pandas as pd

path = "CH-98 Data Cleaning.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1)
test = pd.read_excel(path, usecols="D:F", skiprows=1)

input = input["Description"].str.split(", ", expand=True)
result = pd.DataFrame(columns=["Date", "Product", "Quantity"])

for i in range(len(input)):
    temp = input.iloc[i]
    date = None
    product = None
    quantity = None

    for j in range(temp.size):
        if "/" in temp[j]:
            date = temp[j]
        elif temp[j].isalpha():
            product = temp[j]
        elif temp[j].isdigit():
            quantity = temp[j]
        else:
            if any(char.isalpha() for char in temp[j]):
                product = temp[j]
            if any(char.isdigit() for char in temp[j]):
                quantity = ''.join(filter(str.isdigit, temp[j]))

    result = result._append({"Date": date, "Product": product, "Quantity": quantity}, ignore_index=True)

result["Date"] = pd.to_datetime(result["Date"])
result["Quantity"] = pd.to_numeric(result["Quantity"])
result["Product"] = result["Product"].str.strip()

print(result.equals(test))
