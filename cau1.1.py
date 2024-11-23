# Bài 1: Viết chương trình nhập vào chuỗi ký tự, trả về số các từ trong chuỗi ký tự vừa nhập
# Ví dụ: Nhập vào: “Hom nay    troi   mua   ”          Trả về: 4
chuoi_ki_tu = str(input("nhập vào chuỗi kí tự: "))
dem_so_tu = 0
trong_tu = False
for tu in chuoi_ki_tu :
    if tu != " ":
        if trong_tu == False:
            dem_so_tu = dem_so_tu + 1
            trong_tu = True
    else:
        trong_tu = False

print("so tu trong chuoi la: ",dem_so_tu)