def Reverse_String(Name):
    if Name == "":
        return ""
    else:
        return Reverse_String(Name[1:]) + Name[0]
print(Reverse_String("reverse")       
def Palindrome(Name):
    Name = Name.lower()
    Length = len(Name)
    if Length == 1:
        return True
    else:
        return (Name[0] == Name[Length - 1] and Palindrome(Name[1:Length - 1]))
print(Palindrome("Radar"))
