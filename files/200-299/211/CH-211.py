import pandas as pd

path = "CH-211Column Splitting.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=7)
test = pd.read_excel(path, usecols="D:F", skiprows=1, nrows=7).fillna("").astype(str)

def split_string(series):
    def get_parts(s):
        s = str(s)
        n = len(s)
        if n <= 3:
            return [s, "", ""]
        elif n <= 6:
            mid = (n + 1) // 2
            return [s[:mid], s[mid:], ""]
        else:
            return [s[:3], s[3:6], s[6:]]
    
    result = [get_parts(x) for x in series]
    return pd.DataFrame(result, columns=["Part 1", "Part 2", "Part 3"]).astype(str)

result = split_string(input["ID"])

print(result.equals(test)) # True