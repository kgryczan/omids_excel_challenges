import pandas as pd

path = "400-499/424/CH-424 Replacement.xlsx"
input = pd.read_excel(path, usecols="B:D", nrows=7, skiprows=2)
test = pd.read_excel(path, usecols="F:H", nrows=7, skiprows=2)
test.columns = test.columns.str.replace(r"\.1$", "", regex=True)

result = input.copy()
result["Product ID"] = (
    result["Product ID"].astype(str).str.translate(str.maketrans("ABC", "BCA"))
)

print(result.equals(test))
# True
