import pandas as pd
from io import StringIO

path = "300-399/399/CH-399 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="B", nrows=6, skiprows=3, header=None)
test = pd.read_excel(path, usecols="D:G", nrows=6, skiprows=2)


result = (
    input.stack()
      .dropna()
      .map(lambda x: pd.read_csv(StringIO(x), sep="\t"))
      .pipe(lambda s: pd.concat(s.tolist(), ignore_index=True))
)

print(result.equals(test))
# True