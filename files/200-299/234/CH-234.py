import pandas as pd

path = "200-299/234/CH-234 Column Splitting.xlsx"

input = pd.read_excel(path, usecols="B", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="D:G", skiprows=1, nrows=6)

split_cols = input.iloc[:, 0].str.split("-", n=5, expand=True)
split_cols.columns = ["ID.1", "ID.1.5", "ID.2", "ID.2.5", "ID.3", "ID.4"]
result = pd.DataFrame({
    "ID.1": split_cols["ID.1"] + "-" + split_cols["ID.1.5"],
    "ID.2": split_cols["ID.2"] + split_cols["ID.2.5"].apply(lambda x: f"-{x}" if pd.notna(x) and x != "" else ""),
    "ID.3": split_cols["ID.3"],
    "ID.4": split_cols["ID.4"]
})

print(result)