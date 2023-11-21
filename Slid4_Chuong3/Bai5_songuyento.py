def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True


a = int (input("Nhap so nguyen duong a: "))

if is_prime(a):
    print(a, "la so nguyen to")
else:
    print(a, "khong phai la so nguyen to")
