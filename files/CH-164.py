import pandas as pd
import re

path = "CH-164 Extract from Text.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="E:F", skiprows=1, nrows=6)

def max_depth(S):
    get_chars = lambda string: pd.DataFrame({'pos': range(1, len(string) + 1), 'char': list(string)})
    
    check = -1 if re.match(r'^[{]+[0-9,]+[}]+$', S) else 0
    df = get_chars(S)
    
    df['cum_sum'] = df['char'].apply(lambda x: 1 if x == '{' else (-1 if x == '}' else 0)).cumsum()

    max_depth = df['cum_sum'].max() + check
    
    return max_depth

input['depth'] = input['Value'].apply(max_depth)

print(input['depth'].equals(test['Depth'])) # True