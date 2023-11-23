a = 80
b = 100
print(f"Các số chia hết cho 2 và 3 trong đoạn từ {a} đến {b} là: ")
for i in range(a, b+1):
    if i%2==0 and i%3==0:
        print(i)
        