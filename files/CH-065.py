import pandas as pd

input = pd.read_excel("CH-065 Transformation.xlsx", sheet_name="Sheet1", usecols="B:D", skiprows=1, nrows = 4)
test = pd.read_excel("CH-065 Transformation.xlsx", sheet_name="Sheet1", usecols="F:G", skiprows=1, nrows = 10)

result = input.assign(seq = input.apply(lambda row: pd.date_range(start=row['From'], end=row['TO'], freq='D'), axis=1),
                      len = (input['TO'] - input['From'] + pd.Timedelta(days=1)).dt.days,
                      avg_cost = input['Cost'] / ((input['TO'] - input['From'] + pd.Timedelta(days=1)).dt.days))\
                    .explode('seq')\
                    .drop(columns=['From', 'TO', 'len', 'Cost'])\
                    .rename(columns={'seq': 'Date', 'avg_cost': 'AVG Cost'})\
                    .astype({'AVG Cost': 'int64'})\
                    .reset_index(drop=True)

print(result.equals(test)) # True
