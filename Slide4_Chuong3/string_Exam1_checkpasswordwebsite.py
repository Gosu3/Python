import re

def valid_password (password):
    if len(password) < 6 or len(password) > 12:
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    return True


user = input("Nhập tên đăng nhập: ")
password = input ("Nhập mật khẩu: ")


if valid_password(password):
    print("Đăng nhập thành công vào hệ thống")
else:
    print("Sai thông tin đăng nhập")