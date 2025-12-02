import pandas as pd
import re

path = "300-399/335/CH-335 Table Transformation.xlsx"
df = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=6)
test_df = pd.read_excel(path, usecols="G:H", skiprows=1, nrows=10).rename(columns=lambda c: c.replace('.1', ''))

result = pd.DataFrame(
    [{"Issue ID": r["Issue ID"], "Level": re.match(r"^[^0-9]+", r["Level"]).group(0) + n}
     for _, r in df.iterrows()
     if isinstance(r["Level"], str)
     for n in re.findall(r"\d+", r["Level"])]
)

print(result.equals(test_df))
