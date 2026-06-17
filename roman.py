def a(romannumber):
    
    roman = {'M':1000, "D":500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

    result_integer = 0

    for i in range(len(romannumber)-1):
        if roman[romannumber[i]]<roman[romannumber[i+1]]:
            result_integer -= roman[romannumber[i]]
        elif roman[romannumber[i]]==roman[romannumber[i+1]]:
            result_integer += roman[romannumber[i]]
        else:
            result_integer += roman[romannumber[i]]
        print(result_integer)
    return result_integer + roman[romannumber[-1]]
    
roman = input('Enter your roman numeral: ')
print(f"The integer equivalent of {roman} is: {a(roman)}")