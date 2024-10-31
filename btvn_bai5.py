nhap_ky_tu = str(input("nhap ky tu can xac dinh: "))
if 'a' <= nhap_ky_tu <= 'z':
    if nhap_ky_tu == 'u' and 'e' and 'o' and 'a' and 'i':
        print("day la nguyen am")
    else: 
        print("day la phu am")
else:
    print("day khong la mot chu cai")