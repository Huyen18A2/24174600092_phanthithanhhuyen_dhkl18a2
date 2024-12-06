#Bài 4: Viết chương trình sinh ra ma trận K kích cỡ m*n chỉ chứa số 0
m = int(input("nhập vào số cột của ma trận m = "))
n = int(input("nhập vòa số hàng của ma trận n = "))
ma_tran_a = [[0,0,0],
             [0,0,0],
             [0,0,0]]
ma_tran_a = []
for hang in range(n):
    phan_tu_trong_hang = []
    for cot in range(m):
        phan_tu_trong_hang.append(0)
    ma_tran_a.append(phan_tu_trong_hang)
print(ma_tran_a)

ma_tran_a = [[0]*m]*n 
print(ma_tran_a)