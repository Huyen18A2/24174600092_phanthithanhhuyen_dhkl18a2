# Ví dụ: Nhập vào: “Hom nay    troi   mua   ”
#              Trả về: “Hom nay troi mua”
chuoi_ki_tu = input("nhập chuỗi kí tự: ")
xoa_space_thua = ""
trong_tu = False
for chu in chuoi_ki_tu :
    if chu != " ":
        if trong_tu:  
            xoa_space_thua += chu  
        else:  
            if xoa_space_thua:  
                xoa_space_thua += " "  
            xoa_space_thua += chu  
            trong_tu = True      
    else:
          trong_tu = False  
print("chuỗi kí tự mới là: ", xoa_space_thua)