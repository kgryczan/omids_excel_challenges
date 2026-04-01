import pandas as pd

path = "300-399/390/CH-390 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="B:E", nrows=4, skiprows=2)
test = pd.read_excel(path, usecols="G:I", nrows=7, skiprows=2)

input.columns = input.columns.astype(str)
input = input.rename(columns={input.columns[0]: "col1"})

long = input.melt(id_vars=["col1"], var_name="col", value_name="val")
wide = long.pivot_table(index="col", columns="col1", values="val", aggfunc="first").reset_index()
wide.columns.name = None
wide = wide.assign(Dates=wide["Dates"].astype(str).str.split(r",\s*"))

result = (
    wide.explode("Dates")
    .reset_index(drop=True)
    .loc[:, ["Dates", "Customer", "Product"]]
    .rename(columns={"Dates": "Date"})
)

s = result["Date"].astype(str).str.strip()
is_num = s.str.fullmatch(r"\d+")
date_num = pd.to_datetime(s.where(is_num).astype(float), unit="D", origin="1899-12-30", errors="coerce")
date_dmy = pd.to_datetime(s.where(~is_num), dayfirst=True, errors="coerce")
date_mdy = pd.to_datetime(s.where(~is_num), dayfirst=False, errors="coerce")
result["Date"] = date_num.fillna(date_dmy).fillna(date_mdy)

# transformation technically correct. one extra row in the result and incosistence in the date format.