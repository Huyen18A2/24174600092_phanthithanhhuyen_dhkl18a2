import math
x = float(input("nhap vao gia tri cua x: "))
if x >= -1:
    print(" gia tri x thoa man")
    f_x = (-x + (x**2 + 4)**(1/2))/((x**4 + 1)**(1/7))
    print(f"gia tri cua f(x) = {f_x:.2f}")
else:
    print("gia tri x khong thoa man")

print("ket thhuc chuong trinh")
 