import pandas as pd
import re

input1 = pd.read_excel("CH-056 Process Efficiency.xlsx", usecols = "B:E", nrows = 41, skiprows = 1)
input2 = pd.read_excel("CH-056 Process Efficiency.xlsx", usecols= "G:H", nrows = 4, skiprows = 1)
test = pd.read_excel("CH-056 Process Efficiency.xlsx", usecols="J:K", nrows = 5, skiprows = 1)

result = input1.groupby("Production Id").agg(
    real_sequence=("Machinary", lambda x: ", ".join(x)),
    process_type=("Process type", "first")
).merge(input2, left_on="process_type", right_on="process type").assign(
    aR=lambda x: x["real_sequence"].str.count("A"),
    bR=lambda x: x["real_sequence"].str.count("B"),
    cR=lambda x: x["real_sequence"].str.count("C"),
    dR=lambda x: x["real_sequence"].str.count("D"),
    eR=lambda x: x["real_sequence"].str.count("E"),
    aT=lambda x: x["Sequence"].str.count("A"),
    bT=lambda x: x["Sequence"].str.count("B"),
    cT=lambda x: x["Sequence"].str.count("C"),
    dT=lambda x: x["Sequence"].str.count("D"),
    eT=lambda x: x["Sequence"].str.count("E")
).filter(regex=r"[a-e][RT]").sum().to_frame().T

result2 = pd.DataFrame({
    "machinerty": ["A", "B", "C", "D", "E"],
    "returne_to_back_again_percent": [
        (result["aR"] - result["aT"]) / result["aT"],
        (result["bR"] - result["bT"]) / result["bT"],
        (result["cR"] - result["cT"]) / result["cT"],
        (result["dR"] - result["dT"]) / result["dT"],
        (result["eR"] - result["eT"]) / result["eT"]
    ]
})
result2["returne_to_back_again_percent"] = result2["returne_to_back_again_percent"].apply(lambda x: round(x, 2))
test.columns = result2.columns

print(result2.equals(test)) # True
