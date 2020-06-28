def Sum(Number):
    if (Number == 1):
        return 1
    return Number + Sum(Number-1)
print(Sum(9))
