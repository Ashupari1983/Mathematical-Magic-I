def print_factors(number):
    for i in range(1, number+1):
        if number%i == 0:
            for x in range(2, i):
                if i%x == 0:
                  break
            else:
                print(i)


            

num = int(input('Enter your number: '))
print_factors(num)