import math
x = float(input("nhap gia tri cua x: "))
if x > 0 and x != 1:
    f_x = math.log(x, 4) + math.log(2, x)
    f_x_rounded = round(f_x, 2)
    print(f"gia tri can tim f(x) = {f_x:.2f}")
else:
    print("gia tri x khong thoa man")

print("ket thuc chuong trinh")