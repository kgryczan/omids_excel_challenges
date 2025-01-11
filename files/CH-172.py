import pandas as pd
import time

path = "CH-172 Performance  Optimization.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=249999)
test = pd.read_excel(path, usecols="E:F", skiprows=1, nrows=5).rename(columns=lambda x: x.split('.')[0])

start_time = time.time()
input = input.sort_values(by="Date Houre").assign(Value_diff=lambda x: x['Value'] - x['Value'].shift(1))
result = input.nlargest(5, "Value_diff").sort_values(by="Value", ascending=False).reset_index(drop=True).drop(columns=["Value_diff"])
end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")
# Execution time: 0.0416 seconds
                                                            
print(result.equals(test)) # True