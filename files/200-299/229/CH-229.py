import pandas as pd
import numpy as np

path = "200-299/229/CH-229 Custom Grouping.xlsx"
mean = 463

input_data = pd.read_excel(path, usecols="B", skiprows=1, nrows=101)

percentages = np.arange(0.1, 1.1, 0.1)
ranges = []

for perc in percentages:
    input_data['dist'] = abs(input_data.iloc[:, 0] - mean)
    d = input_data.nsmallest(int(np.ceil(len(input_data) * perc)), 'dist').iloc[-1, 1]
    ranges.append(f"{mean - d}-{mean + d}")

result = pd.DataFrame({
    'pc': percentages,
    'Range': ranges
})

print(result)
