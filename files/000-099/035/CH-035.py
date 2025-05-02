import pandas as pd

input = pd.read_excel("CH-035 Up and Down Grades.xlsx", sheet_name="Sheet1", usecols="B:D", skiprows=1)
test = pd.read_excel("CH-035 Up and Down Grades.xlsx", sheet_name="Sheet1", usecols="H:K", skiprows=1, nrows=4)

result = input.assign(
    Month=pd.to_datetime(input['Date']).dt.to_period('M'),
    Grade=pd.Categorical(input['Grade'], categories=["A+", "A", "B", "C"], ordered=True)
).groupby(['Agent-id', 'Month']).agg(last_grade=('Grade', 'last')).reset_index()

result['prev_grade'] = result.groupby('Agent-id')['last_grade'].shift()
result = result.dropna(subset=['prev_grade'])

grades = {"A+": 4, "A": 3, "B": 2, "C": 1}
result['prev_grade'] = result['prev_grade'].map(grades)
result['last_grade'] = result['last_grade'].map(grades)
result['transition'] = ['Upgrade' if x > y else 'Down-grade' if x < y else 'No Change' for x, y in zip(result['last_grade'], result['prev_grade'])]

result['Month'] = result['Month'].dt.month
result = result.groupby(['transition', 'Month']).size().reset_index(name='transitions')
result = result.pivot(index='Month', columns='transition', values='transitions').fillna(0).reset_index().sort_values('Month')
result = result[['Month', 'Upgrade', 'No Change', 'Down-grade']].astype({"Upgrade": "int64", "No Change": "int64", "Down-grade": "int64"})

print(result == test)  # Discrepancy in month 3
