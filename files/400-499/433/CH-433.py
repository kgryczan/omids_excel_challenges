input_data = {"Number": [135, 518, 175, 5187, 462, 9474, 4387]}
test = {"is_disarium": [True, True, True, False, False, False, False]}


def is_disarium(num):
    digits = [int(digit) for digit in str(num)]
    sum_of_powers = sum(digit**power for power, digit in enumerate(digits, start=1))
    return sum_of_powers == num


result = {
    "Number": input_data["Number"],
    "is_disarium": [is_disarium(num) for num in input_data["Number"]],
}

print(result["is_disarium"] == test["is_disarium"])
# True
