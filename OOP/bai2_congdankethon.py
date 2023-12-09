from datetime import datetime

class CongDanKetHon:
    def __init__(self, ho_ten, ngay_sinh, gioi_tinh, dia_chi, so_cmnd, tinh_trang_doc_than=True):
        self.ho_ten = ho_ten
        self.ngay_sinh = datetime.strptime(ngay_sinh, "%Y-%m-%d").date()
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi
        self.so_cmnd = so_cmnd
        self.tinh_trang_doc_than = tinh_trang_doc_than

    def tinh_tuoi(self):
        today = datetime.now().date()
        age = today.year - self.ngay_sinh.year - ((today.month, today.day) < (self.ngay_sinh.month, self.ngay_sinh.day))
        return age

    def kiem_tra_dieu_kien_ket_hon(self, doi_tac):

        if self.tinh_trang_doc_than and doi_tac.tinh_trang_doc_than:
            if (self.gioi_tinh == "Nam" and self.tinh_tuoi() >= 20) or \
                    (self.gioi_tinh == "Nữ" and self.tinh_tuoi() >= 18):
                if (doi_tac.gioi_tinh == "Nam" and doi_tac.tinh_tuoi() >= 20) or \
                        (doi_tac.gioi_tinh == "Nữ" and doi_tac.tinh_tuoi() >= 18):
                    return True
        return False


cong_dan1 = CongDanKetHon("Nguyen Van A", "1990-01-01", "Nam", "Hanoi", "123456789", True)
cong_dan2 = CongDanKetHon("Nguyen Thi B", "1995-02-15", "Nữ", "Hanoi", "987654321", True)

if cong_dan1.kiem_tra_dieu_kien_ket_hon(cong_dan2):
    print(f"{cong_dan1.ho_ten} và {cong_dan2.ho_ten} đủ điều kiện kết hôn.")
else:
    print(f"{cong_dan1.ho_ten} và {cong_dan2.ho_ten} không đủ điều kiện kết hôn.")
