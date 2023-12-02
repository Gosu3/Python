import re

def validate_password (password):
    if len(password) < 6 or len(password) > 12:
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False

    return True


user_input= input("Nhập tên đăng nhập: ")
password_input = input ("Nhập mật khẩu: ")

passwords_std = password_input.split(",")

#kiểm tra mật khẩu hợp lệ
check_true = [password for password in passwords_std if validate_password(password)]

if check_true:
    print("Mật khẩu hợp lệ là: ", ", ".join(check_true)) #Loại bỏ "['...'] trong chuỗi
    print("Đăng nhập thành công vào hệ thống")
else:
    print("Sai thông tin đăng nhập")