n = int(input("Nhap vao so nguyen n = "))

if n >= 20:
    print("So nhap vao phai nho hon 20!")
    
else:
    print("Cac so chia het cho 5 hoac chia het cho 7 la: ")
    for i in range(1, n+1):
        if i%5==0 or i%7==0:
            print(i)
        
