print("tính cước phí taxi")
tong_tien = 0 
so_km = float(input("số km đã đi:"))
loai_xe =input("nhập loại xe: ")
so_phut_cho = float(input("nhập số phút chờ: "))
if loai_xe == "4":
    if so_km <= 0.8:
        tong_tien_di = 11000
    elif so_km <= 20:
        tong_tien_di = 11000 + (so_km - 0.8) * 12100
    else:
        tong_tien_di = 11000 + (20 - 0.8) * 12100 + (so_km - 20) * 10000
elif loai_xe == "7":
    if so_km <= 0.8:
        tong_tien_di = 13000
    elif so_km <= 30:
        tong_tien_di = 13000 + (so_km - 0.8) * 14100
    else:
        tong_tien_di = 13000 + (30 - 0.8) * 14100 + (so_km - 30) * 12000
else:
    print("loại xe không hợp lệ")

if so_phut_cho > 5:
    so_tien_cho = (so_phut_cho - 5) * 800
tong_tien = so_tien_cho + tong_tien_di

print("cước phí taxi là:" , tong_tien, "đồng")