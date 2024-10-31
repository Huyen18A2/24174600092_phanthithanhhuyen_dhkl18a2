print("đây là các thể loại phim hiện đang có trong rạp chiếu phim ABC")
print("1. phim tình cảm")
print("2. phim kinh dị")
print("3. phim hoạt hình")
print("4. phim khoa học viễn tưởng")
chon = int(input("vui lòng chọn số tương ứng với thế loại bạn muốn xem: "))
if chon == 1:
    print("bạn đã chọn thể loại phim tình cảm")
elif chon == 2:
    print("bạn đã chọn thể loại phim kinh dị")
elif chon == 3:
    print("bạn đã chọn thể loại phim hoạt hình")
elif chon == 4:
    print("bạn đã chọn thể loại phim khoa học viễn tưởng")
else:
    print("lựa chọn của bạn không hợp lệ ")
    print("vui lòng chọn lại")