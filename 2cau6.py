m = int(input("Nhập vào số cột của ma trận m = "))
n = int(input("Nhập vào số hàng của ma trận n = "))

# Khởi tạo ma trận A
ma_tran_A = []

# Nhập các phần tử của ma trận
print("Nhập các phần tử của ma trận A:")
for hang in range(n):
    # Nhập một dòng
    phan_tu_trong_hang = []
    for cot in range(m):
        phan_tu = int(input(f"Nhập phần tử tại vị trí ({hang+1},{cot+1}): "))
        phan_tu_trong_hang.append(phan_tu)
    ma_tran_A.append(phan_tu_trong_hang)

# In ma trận A ra màn hình
print("Ma trận A là:")
for row in ma_tran_A:
    print(row)