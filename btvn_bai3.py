import math 
n1 = float(input("so thu nhat: "))
n2 = float(input("so thu hai: "))
n3 = float(input("so thu ba: "))
if n1 >= n2 and n1 >= n3 :
    so_lon_nhat = n1
elif n2 >= n1 and n2 >= n3 :
    so_lon_nhat = n2
else:
    so_lon_nhat = n3

print("so lon nhat la: ", so_lon_nhat)