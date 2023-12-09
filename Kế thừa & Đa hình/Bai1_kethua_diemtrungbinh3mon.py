class Người:
    def __init__(self, họ_tên, ngày_sinh):
        self.họ_tên = họ_tên
        self.ngày_sinh = ngày_sinh

    def nhập(self):
        self.họ_tên = input("Nhập Họ tên: ")
        self.ngày_sinh = input("Nhập Ngày sinh: ")

    def hiển_thị(self):
        print(f"Họ tên: {self.họ_tên}")
        print(f"Ngày sinh: {self.ngày_sinh}")


class ThíSinh(Người):
    def __init__(self, họ_tên, ngày_sinh, số_báo_danh, điểm_toán, điểm_lý, điểm_hóa):
        super().__init__(họ_tên, ngày_sinh)
        self.số_báo_danh = số_báo_danh
        self.điểm_toán = điểm_toán
        self.điểm_lý = điểm_lý
        self.điểm_hóa = điểm_hóa

    def nhập(self):
        super().nhập()
        self.số_báo_danh = input("Nhập Số báo danh: ")
        self.điểm_toán = float(input("Nhập Điểm toán: "))
        self.điểm_lý = float(input("Nhập Điểm lý: "))
        self.điểm_hóa = float(input("Nhập Điểm hóa: "))

    def hiển_thị(self):
        super().hiển_thị()
        print(f"Số báo danh: {self.số_báo_danh}")
        print(f"Điểm toán: {self.điểm_toán}")
        print(f"Điểm lý: {self.điểm_lý}")
        print(f"Điểm hóa: {self.điểm_hóa}")
        print(f"Điểm trung bình: {self.điểm_trung_bình()}")

    def điểm_trung_bình(self):
        return (self.điểm_toán + self.điểm_lý + self.điểm_hóa) / 3


def nhập_danh_sách_thí_sinh():
    danh_sách_thí_sinh = []
    for _ in range(10):
        thí_sinh = ThíSinh("", "", "", 0, 0, 0)
        thí_sinh.nhập()
        danh_sách_thí_sinh.append(thí_sinh)
    return danh_sách_thí_sinh


def hiển_thị_danh_sách_theo_điểm_trung_bình(danh_sách_thí_sinh):
    danh_sách_thí_sinh.sort(key=lambda x: x.điểm_trung_bình(), reverse=True)
    for thí_sinh in danh_sách_thí_sinh:
        thí_sinh.hiển_thị()


def đếm_số_lượng_đạt_chuẩn(danh_sách_thí_sinh):
    số_lượng_đạt_chuẩn = sum(1 for thí_sinh in danh_sách_thí_sinh if thí_sinh.điểm_trung_bình() >= 20)
    return số_lượng_đạt_chuẩn


# Hàm chính
if __name__ == "__main__":
    danh_sách_thí_sinh = nhập_danh_sách_thí_sinh()

    print("\nDanh sách thí sinh theo điểm trung bình giảm dần:")
    hiển_thị_danh_sách_theo_điểm_trung_bình(danh_sách_thí_sinh)

    số_lượng_đạt_chuẩn = đếm_số_lượng_đạt_chuẩn(danh_sách_thí_sinh)
    print(f"\nSố lượng thí sinh đạt chuẩn (điểm trung bình >= 20): {số_lượng_đạt_chuẩn}")
