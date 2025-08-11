import pandas as pd

path = "200-299/276/CH-276 Value COnversion.xlsx"
input = pd.read_excel(path, usecols="B:E", nrows=6, skiprows=1)
test = pd.read_excel(path, usecols="F", nrows=6, skiprows=1).astype({'Converted Value': str})

def convert_base(x, from_base, to_base):
    n = int(x, from_base)
    if to_base == 2: return bin(n)[2:]
    if to_base == 8: return oct(n)[2:]
    if to_base == 10: return str(n)
    if to_base == 16: return hex(n)[2:].upper()

input['Result'] = input.apply(
    lambda row: convert_base(str(row['Number']), int(row['From Base']), int(row['To Base'])),
    axis=1
)

print(input['Result'].equals(test['Converted Value']))