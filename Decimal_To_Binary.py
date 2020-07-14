def Decimal_To_Binary(Decimal):
    if Decimal < 2:
        return Decimal
    else:
        return 10 * (Decimal_To_Binary(Decimal // 2)) + Decimal % 2
    
    
def Decimal_To_Any_Base(Decimal, Base):
    if Decimal < Base:
        return Decimal
    else:
        return  10 * (Decimal_To_Any_Base(Decimal // Base, Base)) + Decimal % Base

print(Decimal_To_Any_Base(11, 8))
