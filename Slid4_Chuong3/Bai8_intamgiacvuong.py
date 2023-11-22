n = int (input("Nhap so dong n= "))
m = int (input("Nhap so cot m= "))


for i in range(n):
    for j in range(min(i+1,m)):
        print("*", end="")
    print()