import pandas as pd

excel_path = "300-399/342/CH-342 Column Splitting.xlsx"
input = pd.read_excel(excel_path, usecols="B", skiprows=2, nrows=6)
test = pd.read_excel(excel_path, usecols="F:G", skiprows=2, nrows=6)

input["ID"] = input["ID"].str.replace(r"([A-Z]{2})([0-9]{2})", r"\1-\2", regex=True)
split_cols = input["ID"].str.split("-", n=1, expand=True)
split_cols.columns = ["ID 1", "ID 2"]
input[["ID 1", "ID 2"]] = split_cols
input["ID 2"] = input["ID 2"].astype("float64")
id1_equal = input['ID 1'].eq(test['ID 1'], fill_value=None) | (input['ID 1'].isna() & test['ID 1'].isna())
id2_equal = input['ID 2'].eq(test['ID 2'], fill_value=None) | (input['ID 2'].isna() & test['ID 2'].isna())

if id1_equal.all() and id2_equal.all():
    print("All correct")