import pandas as pd
import pandas as pd
# Read the Excel file
path = "CH-101 Subsets.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=5)
test = pd.read_excel(path, usecols="H:I", skiprows=1)

ID = input['ID'].tolist()
df = pd.DataFrame(columns=['ID'])
for i in range(0, len(ID)):
    for j in range(i+1, len(ID)):
        for k in range(j+1, len(ID)):
            df = df._append({'ID': sorted([ID[i], ID[j], ID[k]])}, ignore_index=True)
df = df.drop_duplicates()
df['ID2'] = df['ID']
df = df.explode('ID').reset_index(drop=True)
df = df.merge(input, on='ID', how='left')
df['ID2'] = df['ID2'].apply(lambda x: ','.join(map(str, x)))
df = df.drop(columns=['ID'])
df = df.groupby('ID2').sum().reset_index()

df.columns = test.columns
print(df.equals(test)) # True