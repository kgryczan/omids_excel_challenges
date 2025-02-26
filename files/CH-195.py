import pandas as pd

path = "CH-195 Missing Char.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="D", skiprows=1, nrows=6).rename(columns=lambda x: x.split('.')[0])

def transform_text(text):
    chars = text[:2] 
    
    for i in range(2, len(text)):
        char = text[i] 
        cond = ((len(chars) + 1) % 3 == 0) and (char != "/")  
        chars += ('-' if cond else '') + char 
    
    return chars

input['result'] = input.iloc[:, 0].apply(transform_text)

result = input['result'].tolist()
expected = test.iloc[:, 0].tolist()

print(result == expected) # True