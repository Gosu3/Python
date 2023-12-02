from datetime import datetime

class CongDan:
    def __init__(self, ho_ten, ngay_sinh, gioi_tinh, trinh_do_hoc_van, suc_khoe):
        self.ho_ten = ho_ten
        self.ngay_sinh = datetime.strptime(ngay_sinh, "%Y-%m-%d").date()
        self.gioi_tinh = gioi_tinh
        self.trinh_do_hoc_van = trinh_do_hoc_van
        self.suc_khoe = suc_khoe

    def tinh_tuoi(self):
        today = datetime.now().date()
        age = today.year - self.ngay_sinh.year - ((today.month, today.day) < (self.ngay_sinh.month, self.ngay_sinh.day))
        return age

    def kiem_tra_dieu_kien_nhap_ngu(self):

        return 18 <= self.tinh_tuoi() <= 25 and self.trinh_do_hoc_van not in ["Đại học", "Cao đẳng"] and self.suc_khoe == "Tốt"

    def in_giay_bao_nhap_ngu(self):
        if self.kiem_tra_dieu_kien_nhap_ngu():
            print(f"GIẤY BÁO NHẬP NGŨ\nHọ tên: {self.ho_ten}\nNgày sinh: {self.ngay_sinh.strftime('%Y-%m-%d')}\n"
                  f"Giới tính: {self.gioi_tinh}\nTrình độ học vấn: {self.trinh_do_hoc_van}\nSức khỏe: {self.suc_khoe}")
        else:
            print(f"{self.ho_ten} không đủ điều kiện nhập ngũ.")


cong_dan = CongDan("Nguyen Van B", "2000-01-01", "Nam", "Trung học phổ thông", "Tốt")
cong_dan.in_giay_bao_nhap_ngu()
