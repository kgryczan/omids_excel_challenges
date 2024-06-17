import numpy as np

def draw_triangle(n):
    if n % 2 == 0:
        print("Not Possible")
    else:
        x = (n + 1) // 2
        seq = list(range(1, x + 1))       
        mat = np.full((n, x), "", dtype=object)
        for i in range(x):
            mat[i, :seq[i]] = "*"
        for i in range(1, x):
            mat[n - i, :] = mat[i - 1, :]
        print(mat)

draw_triangle(7)