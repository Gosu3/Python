import re
ds = []
count = 0
checksum = False
matk = None
def dang_ky_tai_khoan():
    print("Đăng ký tài khoản người dùng")
    taikhoan = {}
    taikhoan['user'] = input("Nhập thông tin tài khoản: ")
    taikhoan['password'] = input('Nhập mật khẩu: ')
    
    validate_password()
    
    re_pass = input("Mật khẩu không hợp lệ ! Vui lòng nhập lại mật khẩu: ")
    if (re_pass == taikhoan['password']):
        taikhoan['fullname'] = input('Nhập thông tin họ và tên: ')
        taikhoan ['sdt'] = input('Nhập thông tin số điện thoại: ')
        
        taikhoan['matk'] = count + 1
        ds.append(taikhoan)
        print('Bạn tạo thành công tài khoản')
    else:
        print('Nhập sai mật khẩu. vui lòng nhập lại')
def dang_nhap_he_thong():
    print("Bạn chọn chức năng đăng nhập vào hệ thống")
    user = input('Nhập tài khoản: ')
    password = input('Nhập mật khẩu: ')
    
    for user in ds:
        if (taikhoan['user']== user and taikhoan['password'] == password):
            print('Đăng nhập thành công vào hệ thống')
            checksum = True
            matk = taikhoan['matk']
            return
    print('Sai thông tin tài khoản, mật khẩu')
            

def doi_mat_khau():
    print("Bạn chọn chức năng đổi mật khẩu")
    password1 = input('Nhập mật khẩu: ')
    newPass = input('Nhập thông tin mật khẩu mới')
    checkNewPass = input('Nhập lại mật khẩu mới')
    if (checkNewPass == newPass and taikhoan['password']== password1):
        print('Đổi mật khẩu thành công')
    else:
        print('Mật khẩu không hợp lệ!')
def sua_thong_tin_ca_nhan():
    print("Bạn chọn chức năng sửa thông tin cá nhân")
    
def display_menu():
       print(""""Menu
       
       1. Đăng ký tài khoản
       2. Đăng nhập hệ thống
       3. Đổi mật khẩu
       4. Sửa thông tin cá nhân
       5. Thoát khỏi tài khoản
       6. Thoát
""") 


def validate_password (password):
    if len(passuuud) < 6 or len(password) > 12:
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    return True



while True:
    display_menu()
    choice = input ("Bạn hãy lựa chọn từ 1-5: ")
    
    if choice == '1':
        dang_ky_tai_khoan()
    elif choice == '2':
        dang_nhap_he_thong()
    elif choice == '3':
        doi_mat_khau()
    elif choice == '4':
        sua_thong_tin_ca_nhan()
    elif choice == '5':
        sua_thong_tin_ca_nhan()
    elif choice == '6':
        break
    else:
        print("Lựa chọn không hợp lệ. Hãy nhập số từ 1 đến 5.")