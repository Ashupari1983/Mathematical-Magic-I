def to_decimal(binarynum):
    num = 0
    digits = len(binarynum)

    for i in range(digits):
        num += int(binarynum[i]) * (2 ** (digits - i - 1))

    return num

bn = input("Enter Binary Number: ")
print("Decimal:", to_decimal(bn))