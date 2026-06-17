number = int(input("Enter you number:"))

digits = len(str(number))

realno = 0

temp = number

while temp>0:
    digit = temp%10
    realno += digit**digits
    temp //=10

if realno == number:
    print(f"{number} is an armstrong number.")
else:
    print(f"{number} is not an armstrong number.")