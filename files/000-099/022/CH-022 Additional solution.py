import pandas as pd

input_data = pd.read_excel("CH-022 Convert Number To Text.xlsx", usecols="B", skiprows=1, nrows=9)
test = pd.read_excel("CH-022 Convert Number To Text.xlsx", usecols="G:H", skiprows=1, nrows=9)

lookup = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
    17: "seventeen", 18: "eighteen", 19: "nineteen"
}
lookup_tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

def split_and_textify_number(number: str) -> str:
    number = str(number)
    length = len(number)
    if length == 0:
        return ""
    if length == 1:
        return lookup[int(number)]
    if length == 2:
        n = int(number)
        if n < 20:
            return lookup[n]
        first_digit, second_digit = int(number[0]), int(number[1])
        return f"{lookup_tens[first_digit]}-{lookup[second_digit]}"
    if length == 3:
        return f"{lookup[int(number[0])]} hundred {split_and_textify_number(number[1:])}".strip()
    if length == 4:
        return f"{lookup[int(number[0])]} thousand {split_and_textify_number(number[1:])}".strip()
    raise ValueError("Unsupported length")

def textify_number(number):
    text = str(number)
    if "." in text:
        whole, dec = text.split(".", 1)
    else:
        whole, dec = text, ""
    inp_part_text = split_and_textify_number(whole)
    dec_part_text = split_and_textify_number(str(int(dec))) if dec else ""
    result = inp_part_text if not dec_part_text else f"{inp_part_text} point {dec_part_text}"
    return result.capitalize()

result = input_data.assign(Text=input_data["Number"].map(textify_number))
print(result.equals(test))
