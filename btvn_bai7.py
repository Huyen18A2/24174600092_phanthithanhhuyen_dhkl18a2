a1 = float(input("nhập hệ số a1: "))
b1 = float(input("nhập hệ số b1: "))
c1 = float(input("nhập hệ số c1: "))
a2 = float(input("nhập hệ số a2: "))
b2 = float(input("nhập hệ số b2: "))
c2 = float(input("nhập hệ số c2: "))
D = a1 * b2 - a2 * b1
Dx = c1 * b2 - c2 * b1
Dy = a1 * c2 - a2 * c1
if D != 0:
    x = Dx / D
    y = Dy / D
    print("hệ có nghiệm duy nhất: x =", x, ", y =", y)
else:
    if Dx == 0 and Dy == 0:
        print("hệ có vô số nghiệm.")
    else:
        print("hệ vô nghiệm.")