import pandas as pd

path = "200-299/240/CH-240  Clean Up Excel Formulas.xlsx"
df = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=6)

def format_excel_formula_clean(f):
    res, indent = [], 0
    for ch in f:
        if ch == '(':
            indent += 1
            res += ['(\n', '  ' * indent]
        elif ch == ')':
            indent -= 1
            res += ['\n', '  ' * indent, ')']
        elif ch == ',':
            res += [',\n', '  ' * indent]
        else:
            res.append(ch)
    return ''.join(res)

df['broken'] = df['Formula (Unformatted)'].apply(format_excel_formula_clean)

for formula in df['broken']:
    print(formula, '\n')
