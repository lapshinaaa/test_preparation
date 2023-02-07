def sum_of_digits(list_of_ints: list):
    if len(list_of_ints) == 1:
        return list_of_ints[0]

    else:
        sum_of_ints = 0

        for digit in list_of_ints:
            sum_of_ints += digit

        sum_of_ints = str(sum_of_ints)

        return sum_of_digits(list(int(char) for char in sum_of_ints))


digits = []
for _ in str(input()):  # appending all the digits to a list
    digits.append(int(_))

print(sum_of_digits(digits,))
