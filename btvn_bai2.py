import math
print (" nhap toa do M: ")
x = float(input(" x = "))
y = float(input(" y = "))
print (" nhap toa do I: ")
a = float(input(" a = "))
b = float(input(" b = "))
R = float(input(" nhap vao ban kinh R: "))
do_dai_IM = ((x-a)**2+(y-b)**2)**(1/2)
if R >= do_dai_IM:
    print(" True ")
else: 
    print(" False")

print(" ket thuc chuong trinh ")