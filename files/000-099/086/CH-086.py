import pandas as pd
import numpy as np

path = "CH-86 KNN Missing values.xlsx"
input = pd.read_excel(path, usecols="C:F", skiprows=1)
test = pd.read_excel(path, usecols = "I:L", skiprows=1)
test.columns = test.columns.str.replace(".1", "")
test.loc[8, 'Y'] = 43
test = test.astype('Float64')


def fill_missing_values(data):
    def euclidean_distance(row1, row2):
        return np.sqrt(np.sum((row1 - row2) ** 2))

    data_filled = data.copy()
    complete_cases = data.dropna()

    for i in range(data.shape[0]):
        if data.iloc[i].isnull().any():
            distances = []

            for j in range(complete_cases.shape[0]):
                distance = euclidean_distance(data.iloc[i].dropna(), complete_cases.iloc[j][data.iloc[i].notna()])
                distances.append((distance, complete_cases.iloc[j]))

            distances.sort(key=lambda x: x[0])
            nearest_neighbors = [neighbor for _, neighbor in distances[:2]]

            for col in data.columns:
                if pd.isnull(data.iloc[i][col]):
                    values = [neighbor[col] for neighbor in nearest_neighbors]
                    data_filled.loc[i, col] = np.mean(values)

    return data_filled

result = fill_missing_values(input).astype('Float64')

print(result.equals(test)) # True
