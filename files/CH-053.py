import pandas as pd

input = pd.read_excel("CH-053 OEIS Sequence.xlsx", usecols="B:C", skiprows=1, nrows=10)
test = pd.read_excel("CH-053 OEIS Sequence.xlsx", usecols="G:G", skiprows=1)

range = pd.DataFrame({"number": range(101)})

def are_digits_alphabetical(number):
    digits = list(str(number))
    replaced = [input.loc[input["Number"] == int(digit), "Text"].values[0] for digit in digits]
    return replaced == sorted(replaced)

range["is_alphabetical"] = range["number"].apply(are_digits_alphabetical)
range = range[range["is_alphabetical"]].reset_index(drop=True)
range = range["number"]

print(range.equals(test["Customer"])) # True