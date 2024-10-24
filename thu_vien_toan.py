#bài 2
import math
x = float(input("nhap gia tri cua x: "))
f_x = (-x + (x**2 + 4))**(1/2)/(x**4 + 1)**(1/7)
print(f"gia tri cua f(x): {f_x:.2f}")

#bài 4
t = int(input("nhap thoi gian su dung bong den (s): "))
hieu_dien_the = 220
cuong_do_dong_dien = 2.7
cong_suat = t*hieu_dien_the*cuong_do_dong_dien/3600*1000
tien_phai_tra 