import pandas as pd

test = pd.read_excel("CH-30-Risk Analysis.xlsx", usecols="K:L", skiprows=1, nrows=5)

input = pd.read_excel("CH-30-Risk Analysis.xlsx", usecols="C:H", skiprows=2)
input.rename(columns={input.columns[0]: "LH"}, inplace=True)
input = input.melt(id_vars=["LH"], var_name="Cons", value_name="count").dropna()
input['count'] = input['count'].astype(int)

def classify_risk(row):
    L, C = row['LH'], row['Cons']
    if L < 7 and C < 7 and (L + C) < 7:
        return "Very Low"
    elif L < 9 and C < 9 and (L + C) < 9:
        return "Low"
    elif L < 11 and C < 11 and (L + C) < 11:
        return "Moderate"
    elif L < 13 and C < 13 and (L + C) < 13:
        return "High"
    else:
        return "Very High"
    
input['Risk'] = input.apply(classify_risk, axis=1)
input = input.groupby('Risk').agg({'count': 'sum'}).reset_index()
input['Risk'] = pd.Categorical(input['Risk'], categories=["Very Low", "Low", "Moderate", "High", "Very High"], ordered=True)
input.sort_values('Risk', inplace=True)
input.reset_index(drop=True, inplace=True)
input.columns = test.columns

print(input == test) # All True