import pandas as pd
import networkx as nx
from itertools import product

path = "400-499/440/CH-440 - Knight Distance Problem.xlsx"
test = pd.read_excel(path, usecols="L", skiprows=2, nrows=4).rename(
    columns=lambda x: x.strip()
)
test["example Paths"] = test["example Paths"].str.replace(" ", "", regex=False)
start = "A2"
end = "F7"
blocked = {f"{file}{rank}" for file, rank in product("CD", range(1, 7))}
cells = {f"{file}{rank}" for file, rank in product("ABCDEFGH", range(1, 9))} - blocked
moves = [
    (dx, dy) for dx, dy in product((-2, -1, 1, 2), repeat=2) if abs(dx) + abs(dy) == 3
]


def move(cell, dx, dy):
    x = ord(cell[0]) - ord("A") + dx
    y = int(cell[1]) + dy
    if 0 <= x < 8 and 1 <= y <= 8:
        return f"{chr(ord('A') + x)}{y}"


g = nx.Graph()
g.add_nodes_from(cells)
g.add_edges_from(
    (cell, target)
    for cell in cells
    for dx, dy in moves
    if (target := move(cell, dx, dy)) in cells
)
paths = ["->".join(path) for path in nx.all_shortest_paths(g, start, end)]
paths = list(dict.fromkeys(paths))
