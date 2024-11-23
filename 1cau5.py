chuoi = input("Nhập vào chuỗi ký tự: ")
dem_chu_hoa = 0   
dem_chu_thuong = 0 
for ky_tu in chuoi:
    if ky_tu.isupper(): 
        dem_chu_hoa += 1
    elif ky_tu.islower():  
        dem_chu_thuong += 1
print(f"Số chữ cái viết hoa: {dem_chu_hoa}")
print(f"Số chữ cái viết thường: {dem_chu_thuong}")