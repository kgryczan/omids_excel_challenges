import re
import pandas as pd

path = "CH-230 Project scheduling.xlsx"
test = pd.read_excel(path, usecols="F:H", skiprows=1, nrows=10)
input_data = pd.read_excel(path, usecols="B:D", skiprows=2, nrows=9, names=["id", "dur", "pred"])

def parse_rel(text):
    parts = []
    for item in re.sub(r" days?", "", str(text)).split(","):
        item = item.strip()
        if not item or item == "nan":
            continue
        m = re.fullmatch(r"(\d+)(FS|FF)?(?:\+(\d+))?", item)
        pred = int(m.group(1))
        rel_type = m.group(2) or "FS"
        lag = int(m.group(3) or 0)
        parts.append((pred, rel_type, lag))
    return parts

input_data = input_data.sort_values("id").reset_index(drop=True)
input_data["start"] = pd.NaT
input_data["finish"] = pd.NaT
mask = input_data["id"] == 1
input_data.loc[mask, "start"] = pd.Timestamp("2025-04-01")
input_data.loc[mask, "finish"] = input_data.loc[mask, "start"] + pd.to_timedelta(input_data.loc[mask, "dur"] - 1, unit="D")

while input_data["start"].isna().any():
    progress = False
    for idx, row in input_data[input_data["start"].isna()].iterrows():
        if pd.isna(row["pred"]):
            continue
        rels = parse_rel(row["pred"])
        known = input_data.dropna(subset=["finish"]).set_index("id")
        if not all(pred in known.index for pred, _, _ in rels):
            continue
        starts = []
        for pred, rel_type, lag in rels:
            pred_finish = known.loc[pred, "finish"]
            if rel_type == "FS":
                st = pred_finish + pd.Timedelta(days=lag + 1)
            else:
                st = (pred_finish + pd.Timedelta(days=lag)) - pd.Timedelta(days=row["dur"] - 1)
            starts.append(st)
        st = max(starts)
        input_data.loc[idx, "start"] = st
        input_data.loc[idx, "finish"] = st + pd.Timedelta(days=row["dur"] - 1)
        progress = True
    if not progress:
        break

result = input_data[["id", "start", "finish"]].rename(columns={"id": "Task Name", "start": "Start", "finish": "Finish"})
print(result.equals(test))
