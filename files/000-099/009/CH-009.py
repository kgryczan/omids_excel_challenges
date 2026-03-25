import pandas as pd

input_data = pd.read_excel("CH-009.xlsx", usecols="B:D", skiprows=1, nrows=31)
test1 = pd.read_excel("CH-009.xlsx", usecols="F:G", skiprows=1, nrows=4)
test2 = pd.read_excel("CH-009.xlsx", usecols="I:J", skiprows=1, nrows=4)

result = input_data.groupby("Product", as_index=False)["Result"].agg(seq="".join)

def process_pattern1(string):
    string = (string.replace("+--", "3")
                    .replace("--3", "/5")
                    .replace("3+-", "5/")
                    .replace("-3", "/4")
                    .replace("3+", "4/")
                    .replace("/4+", "/5/")
                    .replace("44", "8")
                    .replace("35", "8"))
    digits = [int(ch) for ch in string if ch.isdigit()]
    return max(digits) if digits else 0

def process_pattern2(string):
    string = (string.replace("+-", "2")
                    .replace("-2", "3", 1) if string.startswith("-2") else string)
    if string.endswith("2+"):
        string = string[:-2] + "3"
    string = (string.replace("-3", "4")
                    .replace("22", "4")
                    .replace("32", "5")
                    .replace("23", "5")
                    .replace("44", "8"))
    digits = [int(ch) for ch in string if ch.isdigit()]
    return max(digits) if digits else 0

result1 = result.assign(max_seq=result["seq"].map(process_pattern1))
result2 = result.assign(max_seq=result["seq"].map(process_pattern2))

print(result1["max_seq"].equals(test1.iloc[:, 1]))
print(result2["max_seq"].equals(test2.iloc[:, 1]))
