import numpy as np
import pandas as pd

path = "CH-006.xlsx"
input_data = pd.read_excel(path, usecols="B", skiprows=1, nrows=11)

def kmeans_1d(values, k, max_iter=100):
    x = np.asarray(values, dtype=float)
    centers = np.quantile(x, np.linspace(0, 1, k + 2)[1:-1])
    labels = np.zeros(len(x), dtype=int)
    for _ in range(max_iter):
        new_labels = np.argmin(np.abs(x[:, None] - centers[None, :]), axis=1)
        if np.array_equal(new_labels, labels):
            break
        labels = new_labels
        new_centers = centers.copy()
        for i in range(k):
            pts = x[labels == i]
            if len(pts):
                new_centers[i] = pts.mean()
        if np.allclose(new_centers, centers):
            break
        centers = new_centers
    return labels + 1

result = input_data.copy()
result["C"] = kmeans_1d(result.iloc[:, 0], 2)
result["D"] = kmeans_1d(result.iloc[:, 0], 3)
result["E"] = kmeans_1d(result.iloc[:, 0], 4)
print(result)
