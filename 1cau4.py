# Bài 4: Viết chương trình nhập vào chuỗi ký tự, trả về kết quả đếm số ký tự là chữ,
#  số ký tự là số và số ký tự là ký tự đặc biệt #
# (Không là số, không là chữ) trong chuỗi
chuoi = input("Nhập vào chuỗi ký tự: ")
dem_chu = 0   
dem_so = 0    
dem_ky_tu = 0 
for ky_tu in chuoi:
    if ky_tu.isalpha():  
        dem_chu += 1
    elif ky_tu.isdigit():  
        dem_so += 1
    else:  
        dem_ky_tu += 1
print(f"Số ký tự là chữ: {dem_chu}")
print(f"Số ký tự là số: {dem_so}")
print(f"Số ký tự là ký tự đặc biệt: {dem_ky_tu}")