import pandas as pd

input1 = pd.read_excel("CH-060 Match payments.xlsx", usecols="B:D", skiprows=1, nrows=13)
input2 = pd.read_excel("CH-060 Match payments.xlsx", usecols="F:H", skiprows=1, nrows=6)
test = pd.read_excel("CH-060 Match payments.xlsx", usecols="K:P", skiprows=1, nrows=13)
test.columns = ["ID"] + list(test.columns[1:])

receipts = input1.copy()
receipts["rec_cum"] = receipts["Cost"].cumsum()
receipts["prev_rec_cum"] = receipts["rec_cum"].shift(fill_value=0)

payments = input2.copy()
payments["pay_cum"] = payments["Payment"].cumsum()
payments["prev_pay_cum"] = payments["pay_cum"].shift(fill_value=0)

matches = []
for _, r in receipts.iterrows():
    row_matches = []
    for _, p in payments.iterrows():
        if r["prev_rec_cum"] < p["pay_cum"] and p["prev_pay_cum"] < r["rec_cum"]:
            overlap = min(r["rec_cum"], p["pay_cum"]) - max(r["prev_rec_cum"], p["prev_pay_cum"])
            if overlap > 0:
                row_matches.append((r["ID"], p["ID"], overlap))
    matches.extend(row_matches)

matched = pd.DataFrame(matches, columns=["receipt_id", "payment_id", "match"])
result = matched.pivot_table(index="receipt_id", columns="payment_id", values="match", aggfunc="sum")
result = result.reindex(receipts["ID"]).reset_index().rename(columns={"receipt_id": "ID"})
result.columns.name = None
result = result.astype(object)
value_cols = [c for c in result.columns if c != "ID"]
result[value_cols] = result[value_cols].where(result[value_cols].notna(), None)
mask = result[value_cols].isna().all(axis=1)
for col in value_cols:
    result.loc[mask, col] = "NP"

print(result.equals(test))
