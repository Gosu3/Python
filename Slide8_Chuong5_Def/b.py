def generate_and_print_squared_values():
    # Tạo danh sách chứa giá trị bình phương từ 1 đến 20
    squared_values = [i**2 for i in range(1, 21)]

    # In các giá trị của danh sách trừ 5 mục đầu tiên
    print("Các giá trị của danh sách trừ 5 mục đầu tiên:")
    for value in squared_values[5:]:
        print(value)

# Gọi hàm để tạo và in danh sách
generate_and_print_squared_values()
