import pandas as pd

path = "300-399/CH-300 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=18)
test = pd.read_excel(path, usecols="G:H", skiprows=1, nrows=5)

def custom_grouping(sales):
    res = []
    if sales:
        res.append({'Group': 1, 'Total Sales': sales[0]})
        grp, total, prev = 2, 0, sales[0]
        for i in sales[1:]:
            total += i
            if total >= 2 * prev:
                res.append({'Group': grp, 'Total Sales': total})
                grp += 1
                prev, total = total, 0
        if total:
            res.append({'Group': grp, 'Total Sales': total})
    return pd.DataFrame(res)

result = custom_grouping(input['Sales'].tolist())
print(result.equals(test)) # True