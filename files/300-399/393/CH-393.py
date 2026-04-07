import pandas as pd

path = "300-399/393/CH-393 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="B:E", nrows=6, skiprows=2)
test = pd.read_excel(path, usecols="G:J", nrows=7, skiprows=2)


def transform(input_df: pd.DataFrame) -> pd.DataFrame:
    df = input_df.T.copy()
    df.columns = df.iloc[0]
    df = df.iloc[1:].reset_index(drop=True)

    result = (
        df.melt(id_vars=["Customer", "Product"], var_name="Date", value_name="Sale")
          .dropna(subset=["Sale"])
          .sort_values("Date")
          .assign(Sale=lambda d: pd.to_numeric(d["Sale"], errors="coerce"))
          .loc[:, ["Date", "Customer", "Product", "Sale"]]
          .reset_index(drop=True)
    )
    return result

result = transform(input)
print(result.equals(test))
# True