n = int(input("Nhập số nguyên duong n: "))

while n<=0:
    print("Vui lòng nhập số nguyên dương.")
    n = int(input("Nhập lại số nguyên dương n: "))


result = 1
i = 1

while i<=n:
    result *= i
    i += 1    
print(f"{n}! = ", result)
