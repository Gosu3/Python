n = int(input("Nhap so nguyen n= "))

if n > 10 :
    print("So nhap vao phai be hon 10")

else:
    print(f"Các số chẵn từ 1 đến {n} là: ")
    for i in range(1, n+1):
        if i%2==0:
            print(i)
