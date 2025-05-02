import pandas as pd
from datetime import datetime

path = "CH-108 AVG Cooperation time.xlsx"
input_data = pd.read_excel(path, usecols="B:E", skiprows=1)
test_data = pd.read_excel(path, usecols="J:K", skiprows=1, nrows=2)

result = input_data[input_data["Leave date"] == "-"].copy()

result["Difference"] = (datetime(2024, 8, 16) - result["Employee Date"]).dt.days / 30.4375

result["mean_difference"] = result.groupby("Level")["Difference"].transform("mean")
result = result[["Level", "mean_difference"]].drop_duplicates()

print(result)
#         Level  mean_difference
# 0      Expert        56.542094
# 2  Managerial        56.640657