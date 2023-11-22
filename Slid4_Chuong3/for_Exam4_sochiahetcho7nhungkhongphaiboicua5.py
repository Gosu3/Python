list_num = []

for num in range(2000,3201):
    if num%7==0 and num%5 != 0:
        list_num.append(num) #append(object) thêm vào phần từ trong list rỗng vào cuối danh sách
        
print("Các số chia hết cho 7 nhưng không phải bộ của  5 từ đoạn 2000 đến 3200 là: ")
print(list_num)