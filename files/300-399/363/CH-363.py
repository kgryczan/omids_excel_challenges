aaimport pandas as pd
import numpy as np

path = "300-399/363/CH-363 Matrix Calculation.xlsx"

input_data = pd.read_excel(path,header=None)
input_matrix = input_data.iloc[3:7, 2:7].to_numpy()
test1 = input_data.iloc[3, 9:12].to_numpy()
test2 = input_data.iloc[3, 14:19].to_numpy()
test3 = input_data.iloc[3:7, 22].to_numpy()

par = 16

def find_subvectors_sum_to_par(mat, target_sum):
    results = []
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            for k in range(j, mat.shape[1]):
                subvector = mat[i, j:k+1]
                if np.sum(subvector) == target_sum:
                    results.append(subvector.flatten().tolist())
    for j in range(mat.shape[1]):
        for i in range(mat.shape[0]):
            for k in range(i, mat.shape[0]):
                subvector = mat[i:k+1, j]
                if np.sum(subvector) == target_sum:
                    results.append(subvector.flatten().tolist())

    return results

result = find_subvectors_sum_to_par(input_matrix, par)

print(np.all(result[0] == test1)) # True
print(np.all(result[1] == test2)) # True
print(np.all(result[2] == test3)) # True