import pandas as pd

path = "200-299/294/CH-294 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=16)
test = pd.read_excel(path, usecols="G:H", skiprows=1, nrows=3)

g = c = 1
groups = []
for result in input['Result']:
    groups.append(g)
    c = c + 1 if result == '+' else 1
    if c > 4: g, c = g + 1, 1

input['Group'] = groups
input['Date'] = pd.to_datetime(input['Date'], format='%d/%b/%Y').dt.strftime('%d/%b/%Y')

result = input.groupby('Group').agg(
    Start_Date=('Date', 'first'),
    End_Date=('Date', 'last'),
    number_of_dates=('Date', 'count')
).reset_index(drop=True)

result.loc[result['number_of_dates'] < 4, 'End_Date'] = "NA"
result.loc[result['number_of_dates'] < 4, 'number_of_dates'] = "-"
result['Group'] = result['Start_Date'] + ' - ' + result['End_Date']
result = result[['Group', 'number_of_dates']]

print(result)
print(test)

#                        Group number_of_dates
# 0  01/Jan/2024 - 10/Jan/2024              10
# 1  12/Jan/2024 - 16/Jan/2024               4
# 2           17/Jan/2024 - NA               -
#                        Group number of dates
# 0  01/Jan/2024 - 10/Jan/2024              10
# 1  12/Jan/2024 - 16/Jan/2024               4
# 2           17/Jan/2024 - NA               -