import pandas as pd
from collections import deque

path = "400-499/430/CH-430 - Knight Distance Problem.xlsx"
start = "a2"
input = pd.read_excel(path, usecols="L", nrows=3, skiprows=2)
test = pd.read_excel(path, usecols="M", nrows=3, skiprows=2)
test["Path"] = test["Path"].str.replace(" ", "", regex=False)

blocked = {f"{file}{rank}" for file in "cd" for rank in range(1, 7)}
moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
files = "abcdefgh"


def knight_moves(cell):
    x, y = files.index(cell[0]), int(cell[1]) - 1
    return [
        next_cell
        for dx, dy in moves
        for nx, ny in [(x + dx, y + dy)]
        if 0 <= nx < 8 and 0 <= ny < 8
        if (next_cell := f"{files[nx]}{ny + 1}") not in blocked
    ]


def shortest_path(start, target):
    queue, visited = deque([(start, [start])]), {start}
    while queue:
        current, path = queue.popleft()
        if current == target:
            return path
        for next_cell in knight_moves(current):
            if next_cell not in visited:
                visited.add(next_cell)
                queue.append((next_cell, path + [next_cell]))
    return None


paths_df = pd.DataFrame(
    {
        "path": [
            "->".join(path) if path else None
            for path in map(
                lambda target: shortest_path(start, target), input["Destination"]
            )
        ]
    }
)

print(paths_df["path"].equals(test["Path"]))
# One path is correct but not the same as in given.
