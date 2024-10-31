import math
n = int(input("nhap nam: "))
if n % 400 == 0:
    print("day la nam nhuan")
elif n % 4 == 0 and n % 100 != 0:
    print("day la nam nhuan")
else:
    print("day kkhong la nam nhuan")

print("ket thuc chuong trinh")
