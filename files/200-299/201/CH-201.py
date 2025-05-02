import pandas as pd
import re
import numpy as np

path = "CH-201Column Splitting.xlsx"

input = pd.read_excel(path, usecols="B", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="D:F", skiprows=1, nrows=6)

vowels = set("AEIOU")

def process_id(s):
    is_palindrome = s == s[::-1]
    is_even = len(s) % 2 == 0
    match = re.search(r"[AEIOU]", s)
    vowelloc = match.start() if match else None

    if is_palindrome:
        half = len(s) // 2
        if is_even:
            part1 = s[:half]
            middle = np.NaN
            part2 = s[half:]
        else:
            part1 = s[:half]
            middle = s[half]
            part2 = s[half+1:]
    else:
        if vowelloc is None:
            part1, middle, part2 = s, None, ""
        else:
            part1 = s[:vowelloc]
            middle = s[vowelloc]
            part2 = s[vowelloc+1:]
    return pd.Series({"Part 1": part1, "Middle": middle, "Part 2": part2})

result = input["ID"].apply(process_id)
result = result.reset_index(drop=True)

print(result.equals(test)) # True