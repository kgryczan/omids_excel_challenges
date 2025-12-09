import pandas as pd
import re

path = "300-399\\338\\CH-338 Column Splitting.xlsx"
input = pd.read_excel(path, usecols="B", nrows=5, skiprows=2)
test = pd.read_excel(path, usecols="F:K", nrows=5, skiprows=2)

colname = input.columns[0]

def add_splitter_on_char_change(x):
    pattern = (
        r"(?<=[A-Za-z])(?=[^A-Za-z])|(?<=[^A-Za-z])(?=[A-Za-z])|"
        r"(?<=[0-9])(?=[^0-9])|(?<=[^0-9])(?=[0-9])|"
        r"(?<=[\W_])(?=[^\W_])|(?<=[^\W_])(?=[\W_])"
    )
    return re.sub(pattern, "|", str(x))

split_cols = input[colname].apply(add_splitter_on_char_change).str.split("|")
maxlen = split_cols.map(len).max()
colnames = [f"ID_{i+1}" for i in range(maxlen)]
result = pd.DataFrame(split_cols.tolist(), columns=colnames)

print(result.equals(test)) # one field incorrect in answers provided