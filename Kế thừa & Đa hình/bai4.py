class Nguoi:
    def __init__(self, họ_tên, số_CMND, phòng_ban):
        self.họ_tên = họ_tên
        self.số_CMND = số_CMND
        self.phòng_ban = phòng_ban

    def hiển_thị(self):
        print(f"Họ tên: {self.họ_tên}")
        print(f"Số CMND: {self.số_CMND}")
        print(f"Phòng ban: {self.phòng_ban}")


class BienChe(Nguoi):
    lương_cơ_bản = 560000

    def __init__(self, họ_tên, số_CMND, phòng_ban, bậc_lương):
        super().__init__(họ_tên, số_CMND, phòng_ban)
        self.bậc_lương = bậc_lương

    def hiển_thị(self):
        super().hiển_thị()
        print(f"Bậc lương: {self.bậc_lương}")
        print(f"Lương: {self.tính_lương()} VND")

    def tính_lương(self):
        return self.lương_cơ_bản * self.bậc_lương


class HopDong(Nguoi):
    def __init__(self, họ_tên, số_CMND, phòng_ban, số_giờ, tiền_công_1_giờ):
        super().__init__(họ_tên, số_CMND, phòng_ban)
        self.số_giờ = số_giờ
        self.tiền_công_1_giờ = tiền_công_1_giờ

    def hiển_thị(self):
        super().hiển_thị()
        print(f"Số giờ làm việc: {self.số_giờ}")
        print(f"Lương: {self.tính_lương()} VND")

    def tính_lương(self):
        return self.số_giờ * self.tiền_công_1_giờ



if __name__ == "__main__":
    danh_sách_bien_che = []
    danh_sách_hop_dong = []

    # Nhập danh sách biên chế
    bien_che_1 = BienChe("Nguyễn Văn A", "123456789", "Phòng Kế toán", 3)
    bien_che_2 = BienChe("Trần Thị B", "987654321", "Phòng Nhân sự", 5)

    danh_sách_bien_che.extend([bien_che_1, bien_che_2])

    # Nhập danh sách hợp đồng
    hop_dong_1 = HopDong("Lê Văn C", "456789123", "Phòng Kế toán", 80, 15000)
    hop_dong_2 = HopDong("Phạm Thị D", "321654987", "Phòng Nhân sự", 100, 12000)

    danh_sách_hop_dong.extend([hop_dong_1, hop_dong_2])

    # Hiển thị thông tin và tính lương
    print("Danh sách nhân viên biên chế:")
    for nv in danh_sách_bien_che:
        nv.hiển_thị()
        print("=" * 30)

    print("\nDanh sách nhân viên hợp đồng:")
    for nv in danh_sách_hop_dong:
        nv.hiển_thị()
        print("=" * 30)

    # Tính tổng lương
    tổng_lương_bien_che = sum(nv.tính_lương() for nv in danh_sách_bien_che)
    tổng_lương_hop_dong = sum(nv.tính_lương() for nv in danh_sách_hop_dong)
    tổng_lương_toan_co_quan = tổng_lương_bien_che + tổng_lương_hop_dong

    print(f"\nTổng lương của nhân viên biên chế: {tổng_lương_bien_che} VND")
    print(f"Tổng lương của nhân viên hợp đồng: {tổng_lương_hop_dong} VND")
    print(f"Tổng lương của toàn cơ quan: {tổng_lương_toan_co_quan} VND")
