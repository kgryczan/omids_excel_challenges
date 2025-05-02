import pandas as pd
import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

path = "CH-80 Convex Hulls.xlsx"
input = pd.read_excel(path, usecols="B:C", nrows=24, skiprows = 1)
test = pd.read_excel(path, usecols="E:F", nrows=5, skiprows = 1)
test.columns = ['X', 'Y']

points = input[['X', 'Y']].values

hull = ConvexHull(points)

# Plotting the convex hull
plt.plot(points[:,0], points[:,1], 'o', label='Points')
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-') 

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Convex Hull of DataFrame Points')
plt.legend()
plt.show()

# Validation 
vertices = pd.DataFrame(points[hull.vertices], columns=['X', 'Y']).sort_values(by=['X', 'Y']).reset_index(drop=True)
test = test.sort_values(by=['X', 'Y']).reset_index(drop=True)
print(test.equals(vertices)) # True