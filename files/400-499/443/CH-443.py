import pandas as pd

path = "400-499/443/CH-443 Number Puzzles - Disarium Number.xlsx"
input = pd.read_excel(path, usecols="B", nrows=7, skiprows=2)
test = pd.read_excel(path, usecols="D", nrows=7, skiprows=2)


def is_disarium(n):
    digits = map(int, str(n))
    return n == sum(digit**position for position, digit in enumerate(digits, 1))


candidates = [n for n in range(1_000_001) if is_disarium(n)]
result = (
    input.assign(key=1)
    .merge(pd.DataFrame({"candidate": candidates, "key": 1}), on="key")
    .drop(columns="key")
    .groupby("Number", as_index=True)
    .apply(
        lambda df: pd.Series(
            {
                "result": (
                    df.loc[df["candidate"] < df.name, "candidate"].max()
                    if (df["candidate"] == df.name).any()
                    else df.loc[(df["candidate"] - df.name).abs().idxmin(), "candidate"]
                )
            }
        )
    )
    .reset_index()
)
