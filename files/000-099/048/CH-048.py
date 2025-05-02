import pandas as pd

input = pd.read_excel("CH-048 Transformation.xlsx", usecols = "B", nrows = 20)
test = pd.read_excel("CH-048 Transformation.xlsx",  usecols="E:O", nrows=10, skiprows=1)
test = test.set_index(test.columns[0])
test = test.fillna(0)

input = input["Questions - Combination models"].str.split("+").tolist()
input = input + [x[::-1] for x in input]
input = pd.DataFrame(input, columns=["Model 1", "Model 2"]).assign(Count=1)

result = input.pivot_table(index="Model 1", columns="Model 2", values="Count", aggfunc="sum")
result = result.reindex(input["Model 1"].unique(), columns=input["Model 1"].unique(), fill_value=0)
result = result.fillna(0)

# compare result with test
print(result.values.tolist() == test.values.tolist())