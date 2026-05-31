import pandas as pd
import networkx as nx

path = "400-499/420/CH-420 - Knight Distance Problem.xlsx"
input = pd.read_excel(path, usecols="L", nrows=3, skiprows=2)
test = pd.read_excel(path, usecols="M", nrows=3, skiprows=2)

start = "A2"
moves = [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)]
def chess_to_coord(s):
    return ('abcdefgh'.index(s[0].lower()), int(s[1:]) - 1)
def coord_to_chess(t):
    return 'abcdefgh'[t[0]] + str(t[1] + 1)
def knight_path(start, end, n=8):
    G = nx.Graph()

    for i in range(n):
        for j in range(n):
            for dx, dy in moves:
                u = (i, j)
                v = (i + dx, j + dy)
                if 0 <= v[0] < n and 0 <= v[1] < n:
                    G.add_edge(u, v)
    path = nx.shortest_path(G, chess_to_coord(start), chess_to_coord(end))
    return '->'.join(map(coord_to_chess, path))
result = input['Destination'].apply(lambda dest: knight_path(start, dest))
# different ways found.