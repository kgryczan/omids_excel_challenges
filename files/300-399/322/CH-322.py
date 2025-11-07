import pandas as pd
import re

path = "300-399/322/CH-322 Text Cleaning.xlsx"

input = pd.read_excel(path, usecols="B", skiprows=1, nrows=8)
test = pd.read_excel(path, usecols="D:E", skiprows=1, nrows=8)

result = (
    input
    .assign(
        Level=lambda df: df["Info"]
            .str.extract(r'(?i)level\s*0*(\d+)')[0]  # Remove leading zeros
            .combine_first(df["Info"].str.extract(r'(?i)(ground)')[0])
            .apply(lambda x: int(x) if pd.notnull(x) and re.fullmatch(r'\d+', str(x)) else x),
        Zone=lambda df: df["Info"]
            .str.extract(r'(?i)zone\s*(\d+)')[0]
            .apply(lambda x: int(x) if pd.notnull(x) and re.fullmatch(r'\d+', str(x)) else x)
            .fillna(df["Info"].str.extract(r'(?i)\b(North|South|East|West)\b')[0])
            .fillna("-")
    )
    .drop(columns=["Info"])
)

print(result.equals(test)) # True