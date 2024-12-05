#Bài 2: Nhập vào dãy A gồm n phần tử từ bàn phím. 
#Tính tổng các phần tử trong dãy A
A = []
while True:
    n = input("Nhap vao so phan tu n trong danh sach: ")
    if n.isdigit() == False:
        print("Yeu cau nhap lai so nguyen duong!!")
    else:
        n = int(n)
        break

for i in range(n):
    while True:
        so = input(f"Nhap gia tri so thu {i + 1}: ")
        if so.isdigit() == False:
            print("Yeu cau nhap vao so!!")
        else:
            so = float(so)
            break
    A.append(so)
tong = sum(A)
print(f"tổng các giá trị trong dãy A:{tong} ")