import pandas as pd

path = "CH-071 Extract from Text.xlsx"
input = pd.read_excel(path, usecols = "B", skiprows = 1)
test  = pd.read_excel(path, usecols = "D", skiprows = 1, nrows = 9)

email_regex = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}"

input["Email Address"] = input["Text"].str.findall(email_regex)
output = input[input["Email Address"].str.len() > 0]
output["Email Address"] = output["Email Address"].str[0]
output = output.drop(columns="Text").reset_index(drop=True)

print(output.equals(test)) # True