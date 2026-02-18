import pandas as pd

path = "300-399/368/CH-368 Text Cleaning.xlsx"
input = pd.read_excel(path, usecols="B", nrows = 6, skiprows = 2)
test = pd.read_excel(path, usecols="E", nrows = 6, skiprows =2 )

def mirror_half(s):
     n = len(s)
     best = ""
     for i in range(n):
         for l in range(1, (n - i + 1) // 2 + 1):
             left = s[i:i+l]
             right = s[i+l:i+2*l]
             if left == right[::-1] and len(left) > len(best):
                 best = left
     return best

input["Cleaned"] = input["ID"].apply(mirror_half)
print(input["Cleaned"].equals(test["ID.1"]))
# Last one correct but not according to the expected output.