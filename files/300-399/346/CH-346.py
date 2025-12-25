import pandas as pd
import numpy as np
from collections import Counter

path = "300-399/346/CH-346 Filter.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=2, nrows=8)
test = pd.read_excel(path, usecols="F", skiprows=2, nrows=3).rename(columns=lambda col: col.replace('.1', ''))

def process_id(id_str):
    chars = list(str(id_str))
    last_char = chars[-1]
    char_count = Counter(chars)
    char_count[last_char] = 0
    filtered = {k: v for k, v in char_count.items() if v >= 3}
    return ''.join(chars) if filtered else None

input['processed'] = input['ID'].apply(process_id)
result = input.dropna(subset=['processed'])[['processed']]
result.columns = ['ID']

print(result.reset_index(drop=True).equals(test.reset_index(drop=True)))
