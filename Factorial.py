def Factorial(Number):                                   
    if Number <= 1:                                    #Base Condition
        return 1
    else:
        Number = Number * Factorial(Number - 1)       # Factorial = n*(n-1)(n-2)(n-3)...........
    return Number
print(Factorial(6))                                   #6*5*4*3*2*1 = 720
