class Nguoi:
    def __init__(self, ho_ten, nam_sinh, bang_cap):
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.bang_cap = bang_cap

    def hien_thi(self):
        print(f"Họ tên: {self.ho_ten}")
        print(f"Năm sinh: {self.nam_sinh}")
        print(f"Bằng cấp: {self.bang_cap}")


class NhaKhoaHoc(Nguoi):
    def __init__(self, ho_ten, nam_sinh, bang_cap, chuc_vu, so_ngay_cong, bac_luong):
        super().__init__(ho_ten, nam_sinh, bang_cap)
        self.chuc_vu = chuc_vu
        self.so_ngay_cong = so_ngay_cong
        self.bac_luong = bac_luong

    def hien_thi(self):
        super().hien_thi()
        print(f"Chức vụ: {self.chuc_vu}")
        print(f"Số ngày công trong tháng: {self.so_ngay_cong}")
        print(f"Bậc lương: {self.bac_luong}")

    def sum_luong(self):
        return self.so_ngay_cong * self.bac_luong


class NhanVienPhongThiNghiem(Nguoi):
    def __init__(self, ho_ten, nam_sinh, bang_cap, luong_thang):
        super().__init__(ho_ten, nam_sinh, bang_cap)
        self.luong_thang = luong_thang

    def hien_thi(self):
        super().hien_thi()
        print(f"Lương trong tháng: {self.luong_thang}")

    def sum_luong(self):
        return self.luong_thang



if __name__ == "__main__":
    ds = []

    nha_khoa_học_1 = NhaKhoaHoc("Nguyễn Văn Tho", 1979, "Tiến sĩ", "Giáo sư", 18, 1500)
    nha_khoa_học_2 = NhaKhoaHoc("Pham Van Bo", 1988, "Tiến sĩ", "Phó giáo sư", 16, 1300)

    nhan_vien_thi_nghiem_1 = NhanVienPhongThiNghiem("Thắng David", 1991, "Cử nhân", 1000)
    nhan_vien_thi_nghiem_2 = NhanVienPhongThiNghiem("Trần Văn Lọ", 1996, "Cử nhân", 800)

    ds.extend([nha_khoa_học_1, nha_khoa_học_2, nhan_vien_thi_nghiem_1, nhan_vien_thi_nghiem_2])

    for nhan_vien in ds:
        nhan_vien.hien_thi()
        print(f"Tổng lương đã chi trả: {nhan_vien.sum_luong()} $")
        print("=" * 30)
