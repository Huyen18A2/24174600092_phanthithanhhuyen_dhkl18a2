#vòng lặp trong python
#vòng lặp có giới hạn(vòng lặp for)

#các kểu dữ liệu tuần tự: string, list, tuple, set, dictionary
#range(n) vòng lặp chạy n vòng
for abc in range(10):
    print(abc) 
#range(10) -> 0,1,2,3,4,5,6,7,8,9
#range khi truyền giá trị phải là số nguyên dương
#các giá tị trị trong range sẽ chạy từ 0 - (n-1)

#khi sử dụng vòng lặp nên kết hợp vs câu lẹnh đk
#(khi sử dụng vòng lặp nên có mục đích rõ ràng)

#trong python vòn lặp nên kết hợp sử dụng 3 công cụ: break,continue, else
# break: dừng vòng lặp ngay lặp tức thoạt tại lần lặp gặp break
for i in range(10):
    if i == 4:
        break
    print(i)



# continue: vòng lặp sẽ bỏ qua lần lặp mà ở đâys xuất hieenj continue
# else: vòng lặp sẽ chạy các câu lệnh xử lý của else trong trường hợp vòng lặp k gặp break

#in dãy số các số lẻ nhỏ hơn n
n = int(input("nhập vào số nguyên dương n: "))
for i in range(n): #chuỗi chạy từ 0 đêns (n-1)
    if i%2 == 1:
        print(i)
#in n các số fibonacci
a = 0
b = 1
n = int(input("nhập vào số nguyên dương: "))
for i in range(n):
    print(a)
    sum_a_b = a + b
    a = b
    b = sum_a_b


#vòng lặp không giới hạn(vòng lặp while)