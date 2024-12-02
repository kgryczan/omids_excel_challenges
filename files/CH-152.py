import pandas as pd

path = "CH-152 Extract from Text.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="E:H", skiprows=1, nrows=6)

def split_on_top_level(s):
    chars = list(s)
    level = 0
    current = ""
    result = []
    for char in chars:
        if char == '{':
            level += 1
        if char == '}':
            level -= 1
        if char == ',' and level == 0:
            result.append(current)
            current = ""
        else:
            current += char
    if current:
        result.append(current)
    return result

input['components'] = input['Value'].apply(split_on_top_level)
components = pd.DataFrame(input['components'].tolist())
components.columns = [f"List.{i+1}" for i in range(components.shape[1])]
result = pd.concat([input.drop(columns=['Value', 'components']), components], axis=1)
test.columns = result.columns

result = result.fillna('')
test = test.fillna('')

print(result.equals(test))  # True