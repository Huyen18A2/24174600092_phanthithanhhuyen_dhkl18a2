print("phân loại sinh viên dựa vào kết quả học tập")
diem =str(input("nhập điểm số: "))
if diem == "A":
    print("đây là sinh viên loại xuất sắc")
elif diem == "B":
    print("đây là sinh viên loại giỏi")
elif diem == "C":
    print("đây là sinh viên loại khá")
elif diem == "D":
    print("đây là sinh viên loại trung bình")
elif diem == "E":
    print("đây là sinh viên loại yếu")
elif diem == "F":
    print("đây là sinh viên loại kém")
else:
    print("điểm không hợp lệ")