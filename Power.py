def FastPower(Base, Power):                    #a^b
    global x
    x += 1
    if (Power == 0 or Base == 1):
        return 1
    elif (Power%2 == 0):
        return FastPower(Base*Base, Power/2)
    else:
        return Base*FastPower(Base, Power-1)
print(FastPower(2, 100))
print(x)
