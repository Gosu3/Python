class QuocGia:
    def __init__(self, ten_quoc_gia, vi_tri_dia_ly, ten_thu_do, so_thanh_pho):
        self.ten_quoc_gia = ten_quoc_gia
        self.vi_tri_dia_ly = vi_tri_dia_ly
        self.ten_thu_do = ten_thu_do
        self.so_thanh_pho = so_thanh_pho

    def hien_thi_thong_tin(self):
        print(f"Quốc gia: {self.ten_quoc_gia}")
        print(f"Vị trí địa lý: {self.vi_tri_dia_ly}")
        print(f"Thủ đô: {self.ten_thu_do}")
        print(f"Số thành phố: {self.so_thanh_pho}")

    def tim_kiem_thu_do(self):
        return self.ten_thu_do


class ThanhPho:
    def __init__(self, ten_thanh_pho, vi_tri_dia_ly, so_dan):
        self.ten_thanh_pho = ten_thanh_pho
        self.vi_tri_dia_ly = vi_tri_dia_ly
        self.so_dan = so_dan

    def hien_thi_thong_tin(self):
        print(f"Thành phố: {self.ten_thanh_pho}")
        print(f"Vị trí địa lý: {self.vi_tri_dia_ly}")
        print(f"Số dân: {self.so_dan}")


class HeThongQuanLy:
    def __init__(self):
        self.danhsach_quoc_gia = []

    def nhap_thong_tin_quoc_gia(self):
        pass

    def nhap_thong_tin_thanh_pho(self):
       pass

    def hien_thi_thong_tin_quoc_gia(self):
        for quoc_gia in self.danhsach_quoc_gia:
            quoc_gia.hien_thi_thong_tin()

    def hien_thi_thong_tin_thanh_pho(self):
       pass

    def tim_kiem_thu_do_quoc_gia(self, ten_quoc_gia):
        for quoc_gia in self.danhsach_quoc_gia:
            if quoc_gia.ten_quoc_gia == ten_quoc_gia:
                return quoc_gia.tim_kiem_thu_do()


he_thong = HeThongQuanLy()
he_thong.nhap_thong_tin_quoc_gia()
he_thong.nhap_thong_tin_thanh_pho()
he_thong.hien_thi_thong_tin_quoc_gia()
he_thong.hien_thi_thong_tin_thanh_pho()
he_thong.tim_kiem_thu_do_quoc_gia("Vietnam")
