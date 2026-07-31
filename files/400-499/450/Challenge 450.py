from collections import deque
import pandas as pd

p = "400-499/450/CH-450 - Knight Distance Problem.xlsx"
sheet = pd.read_excel(
    p, sheet_name="Sheet1", usecols="B:J", skiprows=3, nrows=8, header=None
)
board = {
    (chr(96 + c), int(row.iloc[0])): row.iloc[c]
    for _, row in sheet.iterrows()
    for c in range(1, 9)
}
open_squares = {s for s, value in board.items() if value != "x"}
start = next(s for s, value in board.items() if value == "♘")
targets = sorted(
    (int(value), s)
    for s, value in board.items()
    if pd.notna(value) and str(value).replace(".0", "").isdigit()
)
moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]


def all_paths(square, steps, path):
    if not steps:
        return [path] if square == target else []
    x, y = ord(square[0]) - 96, square[1]
    paths = []
    for dx, dy in moves:
        nxt = (chr(96 + x + dx), y + dy)
        if nxt in open_squares and nxt not in path:
            paths += all_paths(nxt, steps - 1, path + [nxt])
    return paths


steps = max(number for number, _ in targets)
target = next(square for number, square in targets if number == steps)
routes = all_paths(start, steps, [start])

print("Paths:", len(routes))
for route in routes:
    print(" -> ".join(f"{x}{y}" for x, y in route))
print("Moves:", len(routes[0]) - 1)
