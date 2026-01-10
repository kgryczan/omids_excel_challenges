import pandas as pd

path = "300-399/354/CH-354 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=2, nrows=7)
test = pd.read_excel(path, usecols="F:G", skiprows=2, nrows=7).rename(columns=lambda col: col.replace('.1', ''))

def custom_transmute(df):
    result = pd.DataFrame()
    result["IDs"] = df["ID"].astype(str)
    result["Sales"] = df["Sales"]
    result.iloc[:-1, result.columns.get_loc("IDs")] = (
        df["ID"].astype(str).values[:-1] + "," + df["ID"].astype(str).values[1:]
    )
    result.iloc[:-1, result.columns.get_loc("Sales")] = (
        df["Sales"].values[:-1] + df["Sales"].values[1:]
    )
    return result

result = custom_transmute(input)
print(result.equals(test))
# True