import pandas as pd
from datetime import datetime, timedelta

path = "200-299/290/CH-290 Flight Planning.xlsx"
input1 = pd.read_excel(path, usecols="B:F", nrows=10, skiprows=1)
input1['ID'] = input1['ID'].astype(int)
input2 = pd.read_excel(path, usecols="H:I", nrows=4, skiprows=1)
input2['Time Zone'] = input2['Time Zone'].str.extract('([0-9]+)').astype(float)

df = (input1.merge(input2, left_on='From', right_on='City')
            .merge(input2, left_on='To', right_on='City', suffixes=('_orig', '_dest')))
df['dep_time_utc'] = pd.to_datetime(df['Departure Time'].astype(str), format='%H:%M:%S')
df['dep_time_utc'] = df['dep_time_utc'] - pd.to_timedelta(df['Time Zone_orig'], 'h')
df['arr_time_utc'] = df['dep_time_utc'] + pd.to_timedelta(df['Duration'].astype(str))
df['arr_time_local'] = df['arr_time_utc'] + pd.to_timedelta(df['Time Zone_dest'], 'h')
df = df[['ID', 'From', 'To', 'dep_time_utc', 'arr_time_utc', 'arr_time_local']]

def find_routes(city='A', time=df.dep_time_utc.min()-timedelta(hours=1), path={}, target='B'):
    if city == target: return [path]
    if city in path or len(path) > 3: return []
    return [r for _, row in df[df.From.eq(city) & df.dep_time_utc.ge(time)].iterrows() 
            for r in find_routes(row.To, row.arr_time_utc, path | {row.From: row.ID}, target)]

df2 = pd.DataFrame(find_routes())

df2 = df2.reset_index(drop=True).melt(ignore_index=False, var_name='City', value_name='ID').dropna(subset=['ID'])
df2['ID'] = df2['ID'].astype(int)
df2 = df2.reset_index().rename(columns={'index': 'Route'})
result = df2.merge(df, on = ['ID'])

g = result.groupby('Route')
dep = g['dep_time_utc'].first()
arr = g['arr_time_utc'].last()
summary = g.agg(ID=('ID', lambda x: ', '.join(x.astype(str))))
summary['Duration'] = (arr - dep).apply(lambda x: f"{int(x.total_seconds()//3600)}:{int((x.total_seconds()%3600)//60):02d}")
summary['Arrival_Time'] = g['arr_time_local'].last().dt.strftime('%H:%M')

summary.index.name = None  # unname index column

print(summary)
#      ID Duration Arrival_Time
# 0  1, 6     5:20        18:35
# 1  3, 9     4:40        20:40
# 2     7     4:45        23:45