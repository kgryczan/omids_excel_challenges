import pandas as pd

path = "200-299/281/CH-281 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=16)
test = pd.read_excel(path, usecols="G:H", skiprows=1, nrows=3).astype({ 'number of dates': str })

input['Date'] = pd.to_datetime(input['Date']).dt.strftime('%d/%b/%Y')
input['cplus'] = (input['Result'].eq('+').cumsum() - 1) // 4 + 1

res = []
for cplus, group in input.groupby('cplus'):
    plus_rows = group[group['Result'] == '+']
    count = len(plus_rows)
    if count < 4:
        group_label = f"{group['Date'].iloc[0]} - NA"
        num_dates = "-"
    else:
        group_label = f"{group['Date'].iloc[0]} - {group['Date'].iloc[-1]}"
        num_dates = str(len(group))
    res.append({'Group': group_label, 'number of dates': num_dates})
result = pd.DataFrame(res).drop_duplicates()

print(result.equals(test)) # True