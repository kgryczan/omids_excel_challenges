import pandas as pd

input_data = pd.read_excel("CH-022 Convert Number To Text.xlsx", usecols="B", skiprows=1, nrows=9)
test = pd.read_excel("CH-022 Convert Number To Text.xlsx", usecols="G:H", skiprows=1, nrows=9)

ones = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
    17: "seventeen", 18: "eighteen", 19: "nineteen"
}
tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

def textify_whole(number: str) -> str:
    if not number:
        return ""
    n = int(number)
    if n < 20:
        return ones[n]
    if n < 100:
        t, o = divmod(n, 10)
        return tens[t] if o == 0 else f"{tens[t]}-{ones[o]}"
    if n < 1000:
        h, rem = divmod(n, 100)
        tail = textify_whole(str(rem)).strip()
        return f"{ones[h]} hundred" if rem == 0 else f"{ones[h]} hundred {tail}"
    th, rem = divmod(n, 1000)
    tail = textify_whole(str(rem)).strip()
    return f"{ones[th]} thousand" if rem == 0 else f"{ones[th]} thousand {tail}"

def textify_number(number):
    text = str(number)
    if "." in text:
        whole, dec = text.split(".", 1)
        out = f"{textify_whole(whole)} point {textify_whole(str(int(dec)))}"
    else:
        out = textify_whole(text)
    return out.capitalize()

result = input_data.assign(Text=input_data["Number"].map(textify_number))
print(result.equals(test))
