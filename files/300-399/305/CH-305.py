import pandas as pd

path = "300-399/305/CH-305 Advanced Calculation.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=17)
test = pd.read_excel(path, usecols="H:I", skiprows=1, nrows=4)

result = input.groupby('Product')['Sales'].apply(
    lambda x: (x.max() - x.min()) / x.drop([x.idxmin(), x.idxmax()]).mean()
)

print(result)
# Different result for Product A