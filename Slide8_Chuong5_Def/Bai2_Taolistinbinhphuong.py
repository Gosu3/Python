def result():
   
    value_list = [i**2 for i in range(1, 21)]


    print("Các giá trị của danh sách trừ 5 mục đầu tiên:")
    for value in value_list[5:]:
        print(value)

result()
