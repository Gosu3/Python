n = int(input("Nhập giá trị của n: "))

print(f"Các số chia hết cho 5 và tận cùng là số 5 từ 1 đến {n} là:")
for i in range(1, n + 1):
    if i % 5 == 0 and i % 10 == 5:
        print(i)

