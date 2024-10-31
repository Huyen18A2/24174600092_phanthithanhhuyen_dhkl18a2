print("tính thuế thu nhập và lương ròng ")
tien_luong = float(input("nhập số tiền lương: "))
if tien_luong >=15:
    thue = 0.3 * tien_luong
elif 7<= tien_luong <15:
    thue = 0.2 * tien_luong
else:
    thue = 0.1 * tien_luong
luong_rong = tien_luong - thue
print("thuế thu nhập là:", thue, "triệu đồng")
print("tiền lương ròng là: ", luong_rong,"triệu đồng")