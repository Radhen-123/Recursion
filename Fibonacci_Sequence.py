def Fibonacci_Sequence(AtLocation):
    if AtLocation<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif AtLocation==0:
        return 0
    # Second Fibonacci number is 1
    elif AtLocation==1:
        return 1
    else:
        return Fibonacci_Sequence(AtLocation-1)+Fibonacci_Sequence(AtLocation-2)


def Fibonacci(NumberOfTerms):
    n = 0
    List = [0, 1]
    while NumberOfTerms-2 != 0:
        List.append(List[n]+List[n+1])
        n += 1
        NumberOfTerms -= 1
    print(List)
Fibonacci(8)
print(Fibonacci_Sequence(7))


