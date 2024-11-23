# Bài 3: Viết chương trình nhập vào họ tên đầy đủ, trả về tên và họ riêng
# Ví dụ: Nhập vào: “Vo Van Nam”
#              Trả về: “Ho: Vo, Ten: Nam”
ho_va_ten = input("nhập vào họ và tên: ")
tach_tung_tu = ho_va_ten.split()
ho = ""
ten = ""
for tu in tach_tung_tu:
    if ho == "":  
        ho = tu
    ten = tu  
print(f"Họ: {ho}, Tên: {ten}")