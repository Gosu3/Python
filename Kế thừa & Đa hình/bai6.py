class Nguoi:
    def __init__(self, ma_so, ho_ten):
        self.ma_so = ma_so
        self.ho_ten = ho_ten
    def hien_thi(self):
        print(f"Mã số: {self.ma_so}")
        print(f"Ho_ten: {self.ho_ten}")
class Giaoviencohuu(Nguoi):
    def __init__(self, ma_so, ho_ten, tien_cong, so_tiet, phu_cap_dac_biet):
        super().__init__(ma_so, ho_ten)
        self.tien_cong = tien_cong
        self.so_tiet = so_tiet
        self.phu_cap_dac_biet = phu_cap_dac_biet
class Nhanvienhanhchinh(Nguoi):
    def __init__(self, ma_so, ho_ten, he_so_luong, phu_cap):
        super().__init__(ma_so, ho_ten)
        self.he_so_luong = he_so_luong
        self.phu_cap = phu_cap
        
class Giaovienthinhgiang(Nguoi):
    def __init__(self, ma_so, ho_ten, tien_cong, so_tiet):
        super().__init__(ma_so, ho_ten)
        self.tien_cong = tien_cong
        self.so_tiet = so_tiet
    
    

    