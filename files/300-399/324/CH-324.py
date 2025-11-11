import pandas as pd
import re

path = "300-399/324/CH-324 Text Cleaning.xlsx"
input_df = pd.read_excel(path, usecols="B", skiprows=1, nrows=7)
test_df = pd.read_excel(path, usecols="D", skiprows=1, nrows=7).rename(columns=lambda col: col.replace('.1', ''))

input_df["Level"] = input_df["Level"]\
    .apply(lambda v: re.sub(r",$", "", re.sub(r"(Under Ground|Upper Ground|Ground)", r"\1,", str(v))) if pd.notna(v) else v)
print(input_df["Level"].equals(test_df["Level"])) # True