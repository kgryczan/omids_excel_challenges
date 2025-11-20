import pandas as pd

path = "300-399\\328\\CH-328 Text Cleaning.xlsx"
input = pd.read_excel(path, usecols="B", nrows = 8, skiprows = 1)
test = pd.read_excel(path, usecols="D", nrows = 8, skiprows = 1); test.columns = [col.replace('.1', '') for col in test.columns]

result = (
    input.assign(
        Level=(
            input["Level"]
            .str.replace("Ground", "Ground,", regex=False)
            .str.replace(",$", "", regex=True)
            .str.split(", ")
            .map(lambda x: ", ".join(pd.unique(pd.Series(x))))
        )
    )
)

print(result.equals(test))
# True