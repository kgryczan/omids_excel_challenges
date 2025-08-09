import pandas as pd
from scipy.spatial.distance import pdist, squareform
import numpy as np

# Easy way (using scipy library)

df = pd.DataFrame({'ID': range(1,16), 'X': [8,2,7,5,2,8,4,7,10,3,6,3,10,8,5], 'Y': [3,8,6,3,2,12,7,2,3,7,9,6,4,3,2]})
coords = df[['X', 'Y']].values
distances = squareform(pdist(coords, metric='euclidean'))

neighbor_counts = np.sum(distances < 3, axis=1) - 1 
df['Neighbors'] = neighbor_counts
df['Is_Noise'] = neighbor_counts < 2

noise_points = df[df['Is_Noise']]['ID'].tolist()
print(','.join(map(str, noise_points)))

# Hard way (Math)
df2 = pd.DataFrame({'ID': range(1,16), 'X': [8,2,7,5,2,8,4,7,10,3,6,3,10,8,5], 'Y': [3,8,6,3,2,12,7,2,3,7,9,6,4,3,2]})
neighbors_count = []
noise_points = []

for i in range(len(df2)):
    count = 0
    for j in range(len(df2)):
        if i != j: 
            dist_sq = (df2.iloc[i]['X'] - df2.iloc[j]['X'])**2 + (df2.iloc[i]['Y'] - df2.iloc[j]['Y'])**2
            if dist_sq < 9:
                count += 1
    
    neighbors_count.append(count)
    if count < 2:
        noise_points.append(df2.iloc[i]['ID'])

# Results

print(','.join(map(str, noise_points)))