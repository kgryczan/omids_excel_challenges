import pandas as pd
from datetime import timedelta
from scipy.interpolate import interpolate

input = pd.read_excel("CH-062 Missing Values.xlsx", usecols="B:D", skiprows=1, nrows=19)
test = pd.read_excel("CH-062 Missing Values.xlsx", usecols="H:J", skiprows=1)
test.columns = test.columns.str.replace('.1', '')

input["Date"] = pd.to_datetime(input["Date"]) + timedelta(days=1)
all_dates = pd.date_range(start=input["Date"].min(), end=input["Date"].max(), freq='MS')
all_dates = pd.DataFrame(all_dates, columns=["Date"])
all_dates["Date"] = pd.to_datetime(all_dates["Date"]) - timedelta(days=1)
input["Date"] = pd.to_datetime(input["Date"]) - timedelta(days=1)

all_projects = pd.DataFrame(input["Project"].unique(), columns=["Project"])

all_dates["key"] = 0
all_projects["key"] = 0
all_dates = all_dates.merge(all_projects, on="key").drop(columns=["key"]).sort_values(["Project","Date"]).reset_index().drop(columns="index")

all_dates = all_dates.merge(input, on=["Project","Date"], how="left")

all_dates["Actual Progress"] = all_dates.groupby("Project")["Actual Progress"].transform(lambda x: x.interpolate())

print(all_dates["Actual Progress"].round(4).equals(test["Actual Progress"].round(4)))
