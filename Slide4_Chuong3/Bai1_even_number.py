#Dùng for và điều kiện if
n = int(input("Nhập số nguyên n: "))

print("Các số chẵn từ 1 đến", n, "là:")
for i in range(1, n+1):
    if i%2==0:
        print(i)
        
        
        
#Sử dụng bước nhảy
n = int(input("Nhập số nguyên n:"))

print("Các số chẵn từ 1 đến", n, "là:")
for i in range(2, n+1, 2):
    print(i)
    
    
#Sử dụng list
n = int(input("Nhập số nguyên n:"))

even_number = [num for num in range(1, n+1) if num%2==0]
print(even_number)

    