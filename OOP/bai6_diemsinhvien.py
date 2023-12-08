class SinhVien:
    def __init__(self, ma_sv, ho_ten, lop, diem_tb):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.lop = lop
        self.diem_tb = diem_tb

    def hien_thi_thong_tin(self):
        print(f"Mã sinh viên: {self.ma_sv}")
        print(f"Họ và tên: {self.ho_ten}")
        print(f"Lớp: {self.lop}")
        print(f"Điểm trung bình: {self.diem_tb}\n")


class DanhSachSinhVien:
    def __init__(self):
        self.danh_sach_sinh_vien = []

    def them_sinh_vien(self, sinh_vien):
        self.danh_sach_sinh_vien.append(sinh_vien)

    def in_danh_sach(self):
        for sinh_vien in self.danh_sach_sinh_vien:
            sinh_vien.hien_thi_thong_tin()

    def sap_xep_theo_diem_tb(self):
        self.danh_sach_sinh_vien.sort(key=lambda x: x.diem_tb, reverse=True)

    def tim_sinh_vien_theo_ma_sv(self, ma_sv):
        for i, sinh_vien in enumerate(self.danh_sach_sinh_vien):
            if sinh_vien.ma_sv == ma_sv:
                return i
        return -1


danh_sach = DanhSachSinhVien()

sv1 = SinhVien("001", "Nguyen Van A", "KTPM", 8.5)
sv2 = SinhVien("002", "Tran Thi B", "CNTT", 9.2)
sv3 = SinhVien("003", "Le Van C", "QTKD", 7.8)

danh_sach.them_sinh_vien(sv1)
danh_sach.them_sinh_vien(sv2)
danh_sach.them_sinh_vien(sv3)

print("Danh sách sinh viên trước khi sắp xếp:")
danh_sach.in_danh_sach()

print("\nDanh sách sinh viên sau khi sắp xếp theo điểm trung bình giảm dần:")
danh_sach.sap_xep_theo_diem_tb()
danh_sach.in_danh_sach()

ma_sv_can_tim = "002"
vi_tri_tim_thay = danh_sach.tim_sinh_vien_theo_ma_sv(ma_sv_can_tim)

if vi_tri_tim_thay != -1:
    print(f"\nTìm thấy sinh viên có mã {ma_sv_can_tim} tại vị trí {vi_tri_tim_thay}")
else:
    print(f"\nKhông tìm thấy sinh viên có mã {ma_sv_can_tim}")
