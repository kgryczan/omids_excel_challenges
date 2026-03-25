from openpyxl import load_workbook
import pandas as pd

path = "CH-024 Hilight merged dcells.xlsx"
wb = load_workbook(path)
ws = wb.active

target_rows = range(2, 15)   # B2:I14 source region
target_cols = range(2, 10)
merged = set()

for merged_range in ws.merged_cells.ranges:
    min_col, min_row, max_col, max_row = merged_range.bounds
    for row in range(max(min_row, 2), min(max_row, 14) + 1):
        for col in range(max(min_col, 2), min(max_col, 9) + 1):
            merged.add((row - 1, col - 1))

rows = []
for r in range(1, 13):
    row = []
    for c in range(1, 9):
        row.append("X" if (r, c) in merged else "")
    rows.append(row)

result = pd.DataFrame(rows)
print(result)
