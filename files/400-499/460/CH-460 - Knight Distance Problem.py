import pandas as pd

path = "400-499/460/CH-460 - Knight Distance Problem.xlsx"
input = pd.read_excel(
    path, sheet_name="Sheet1", header=None, usecols="B:J", skiprows=3, nrows=8
)
board = input.iloc[:, 1:].to_numpy()
cells = {(r, c) for r in range(8) for c in range(8) if board[r, c] != "x"}
moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
neighbours = {
    p: [(p[0] + dr, p[1] + dc) for dr, dc in moves if (p[0] + dr, p[1] + dc) in cells]
    for p in cells
}
start = next((r, c) for r, c in cells if board[r, c] == "♘")
path = [start]


def walk(cell):
    if len(path) == len(cells):
        return True
    for nxt in sorted(
        (p for p in neighbours[cell] if p not in path),
        key=lambda p: sum(q not in path for q in neighbours[p]),
    ):
        path.append(nxt)
        if walk(nxt):
            return True
        path.pop()
    return False


walk(start)
cell = lambda p: f"{chr(65 + p[1])}{8 - p[0]}"
result = pd.DataFrame({"Step": range(len(path)), "Cell": [cell(p) for p in path]})
print(result)
