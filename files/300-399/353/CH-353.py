import pandas as pd
import datetime as dt
import numpy as np

path = "300-399\\353\\CH-353 Appending.xlsx"
input1 = pd.read_excel(path, usecols="B:E", nrows = 3, skiprows = 2)
input2 = pd.read_excel(path, usecols="B:E", nrows = 3, skiprows = 8)
test = pd.read_excel(path, usecols="G:J", nrows=6, skiprows=2)
test.columns = [col.replace('.1', '') for col in test.columns] if any('.1' in col for col in test.columns) else test.columns

def semantic_type(s):
    if pd.api.types.is_datetime64_any_dtype(s): return "date"
    if s.map(type).eq(dt.time).all(): return "time"
    if pd.api.types.is_string_dtype(s): return "character"
    if pd.api.types.is_numeric_dtype(s): return "numeric"
    return "other"

def append_by_semantic_type(base, new):
    bt = [semantic_type(base[c]) for c in base]
    nt = [semantic_type(new[c]) for c in new]
    if sorted(bt) != sorted(nt): raise ValueError("Semantic type mismatch")
    new2 = pd.concat([new[[c for c, t in zip(new, nt) if t == typ]] for typ in bt], axis=1)
    new2.columns = base.columns
    return pd.concat([base, new2], ignore_index=True)

output = append_by_semantic_type(input1, input2)

print(output.equals(test))  # True