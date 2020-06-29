x = 0
def FastPower(Base, Power):                    #a^b
    global x                                   #to count Steps
    x += 1
    if (Power == 0 or Base == 1):             # Baase Condition
        return 1
    elif (Power%2 == 0):
        return FastPower(Base*Base, Power/2)    #example 3^6 = (3*3)^3
    else:
        return Base*FastPower(Base, Power-1)    #example 3^3 = 3*3^2
print(FastPower(2, 100))
print("steps:"+str(x))
