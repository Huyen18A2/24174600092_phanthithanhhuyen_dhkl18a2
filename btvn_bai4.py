import math 
a = float(input("canh a: "))
b = float(input("canh b: "))
c = float(input("canh c: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("day la tam giac đeu")
    elif a == b or b == c or a == c:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("day la tam giac vuong can")
        else:
            print("day tam giac can")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("day la tam giac vuong")
    else:
        print("day la tam giac thuong")
else:
    print("khong phai bo ba canh cua tam giac")
    