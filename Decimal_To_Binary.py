def Decimal_To_Binary(Decimal):
    if Decimal < 2:
        return Decimal
    else:
        return 10 * (Decimal_To_Binary(Decimal // 2)) + Decimal % 2
