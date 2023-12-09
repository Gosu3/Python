class Nguoi:
    def __init__(self, ho_ten, so_CMND, phong_ban):
        self.ho_ten = ho_ten
        self.so_CMND = so_CMND
        self.phong_ban = phong_ban

    def hien_thi(self):
        print(f"Họ tên: {self.ho_ten}")
        print(f"Số CMND: {self.so_CMND}")
        print(f"Phòng ban: {self.phong_ban}")


class BienChe(Nguoi):
    luong_co_ban = 560000

    def __init__(self, ho_ten, so_CMND, phong_ban, bac_luong):
        super().__init__(ho_ten, so_CMND, phong_ban)
        self.bac_luong = bac_luong

    def hien_thi(self):
        super().hien_thi()
        print(f"Bậc lương: {self.bac_luong}")
        print(f"Lương: {self.tinh_luong()} VND")

    def tinh_luong(self):
        return self.luong_co_ban * self.bac_luong


class HopDong(Nguoi):
    def __init__(self, ho_ten, so_CMND, phong_ban, so_gio, tien_cong_1h):
        super().__init__(ho_ten, so_CMND, phong_ban)
        self.so_gio = so_gio
        self.tien_cong_1h = tien_cong_1h

    def hien_thi(self):
        super().hien_thi()
        print(f"Số giờ làm việc: {self.so_gio}")
        print(f"Lương: {self.tinh_luong()} VND")

    def tinh_luong(self):
        return self.so_gio * self.tien_cong_1h



if __name__ == "__main__":
    ds = []

    bien_che_1 = BienChe("Nguyễn Văn Bo", "123498567", "Phòng Kinh doanh", 4)
    bien_che_2 = BienChe("Phạm Thị Ổi", "098765421", "Phòng Nhân sự", 6)
    hop_dong_1 = HopDong("Phan Duy Á", "456789123", "Phòng Kỹ thuật", 90, 16000)
    hop_dong_2 = HopDong("Phạm Thị D", "321654987", "Phòng Vận hành", 120, 14000)

    ds.extend([bien_che_1, bien_che_2, hop_dong_1, hop_dong_2])


    print("Danh sách nhân viên:")
    for nv in ds:
        nv.hien_thi()
        print("=" * 30)

    # Tính tổng lương
    Lbien_che = sum(nv.tinh_luong() for nv in ds if isinstance(nv, BienChe)) 
    Lhop_dong = sum(nv.tinh_luong() for nv in ds if isinstance(nv, HopDong))
    Ltoan_co_quan = Lbien_che + Lhop_dong

    print(f"\nTổng lương của nhân viên biên chế: {Lbien_che} VND")
    print(f"Tổng lương của nhân viên hợp đồng: {Lhop_dong} VND")
    print(f"Tổng lương của toàn cơ quan: {Ltoan_co_quan} VND")
