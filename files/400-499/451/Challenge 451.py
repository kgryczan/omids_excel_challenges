from itertools import groupby
import pandas as pd

file = "400-499/451/CH-451 Column Splitting.xlsx"
input_data = pd.read_excel(file, usecols="B", skiprows=2, nrows=6)
expected = pd.read_excel(file, usecols="F:J", skiprows=2, nrows=6).fillna("")


def split_id(identifier):
    """Return consecutive X/Y runs, e.g. XXYXYX -> XX, Y, X, Y, X."""
    return ["".join(run) for _, run in groupby(identifier)]


result = pd.DataFrame(
    [split_id(identifier) for identifier in input_data["ID"]], columns=expected.columns
).fillna("")

print(result.equals(expected))
