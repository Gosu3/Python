#ước của 1 và chính nó
a = int(input("Nhập số nguyên dương a: "))
while a <= 1:
    print("Vui lòng nhập số nguyên dương a lớn hơn 1")
    a = int(input("Nhập lại số nguyên dương a: "))

is_prime = True
i = 2

while i*i <= a:
    if a%i == 0:
        is_prime = False
        break
    i = i+1

if is_prime:
    print(f"{a} là số nguyên tố")
    
else:
    print(f"{a} không phải là số nguyên tố")