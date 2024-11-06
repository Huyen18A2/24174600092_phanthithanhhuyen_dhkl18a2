# Tính các phép tính sau:
# S1 = 1 + 2 + 3 + 4 + …. + n
n = int(input("Nhập số n: "))
S1 = 0
for i in range(1, n + 1):
    S1 = S1 + i
print("Tổng S1 =", S1)

#S2 = 1*2*3*4*…*(n-1)
n =  int(input("Nhập số n: "))
S2 = 1
for i in range(1, n + 1):
    S2 = S2*i
print("Tích S2 =", S2)

# S3 = 1 – 1/2 + 1/3 – 1/4 + …. + ((-1)**n)/n
n = int(input("Nhập số n: "))
S3 = 0
for i in range(1, n + 1):
    S3 = S3 + (((-1)**(i+1))/i)
print("Tổng S3 =", S3)

#tính tổng k/k+2 từ 0 đến n
n = int(input("Nhập số n: "))
S4 = 0
for i in range(0, n+1):
    S4 = S4 + (i/(i+2))
print("Tổng S4 =", S4)