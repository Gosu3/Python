def generate_employee_id(full_name, birth_year, work_year, existing_ids):
    # Lấy chữ cái đầu tiên của họ và tên
    initials = ''.join(word[0] for word in full_name.split())

    # Lấy hai chữ số cuối cùng của năm sinh
    birth_year_last_two_digits = str(birth_year)[-2:]

    # Lấy hai chữ số cuối cùng của năm làm việc
    work_year_last_two_digits = str(work_year)[-2:]

    # Kết hợp các thành phần để tạo mã nhân viên
    employee_id = f"{initials.upper()}{birth_year_last_two_digits}{work_year_last_two_digits}"

    # Kiểm tra xem mã nhân viên đã tồn tại chưa
    if employee_id in existing_ids:
        # Nếu tồn tại, tăng giá trị đếm
        count = 1
        while f"{employee_id}{count}" in existing_ids:
            count += 1
        employee_id = f"{employee_id}{count}"

    return employee_id

# Sử dụng hàm
existing_ids = set()  # Danh sách mã nhân viên đã tồn tại
full_name = input("Nhập Họ tên: ")
birth_year = int(input("Nhập Năm sinh: "))
work_year = int(input("Nhập Năm làm việc: "))

employee_id = generate_employee_id(full_name, birth_year, work_year, existing_ids)
existing_ids.add(employee_id)  # Thêm mã mới vào danh sách đã tồn tại
print("Mã nhân viên được sinh ra:", employee_id)