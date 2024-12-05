A = []
B = []
while True:
    n = input("Nhập vào số nguyêb dương n: ")
    if n.isdigit() == False:
        print("Yeu cau nhap lai so nguyên dương!!")
    else:
        n = int(n)
        break

for i in range(1,n,2):
    A.append(i)
for j in range(0,n,2):
    B.append(j)
A.reverse()
B.reverse()
    
print("dsa",A)
print("dsb",B)