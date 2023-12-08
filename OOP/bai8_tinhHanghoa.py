
     
class HangHoa:
    def __init__(self, ma_hang, ten_hang, don_gia, so_luong):
        self.__ma_hang = ma_hang
        self.__ten_hang = ten_hang
        self.__don_gia = don_gia
        self.__so_luong = so_luong

    def tinh_thanh_tien(self):
        return self.__so_luong * self.__don_gia

    def hien_thi_thong_tin(self):
        print(f"Mã hàng: {self.__ma_hang}")
        print(f"Tên hàng: {self.__ten_hang}")
        print(f"Đơn giá: {self.__don_gia} $")
        print(f"Số lượng: {self.__so_luong}")
        print(f"Thành tiền: {self.tinh_thanh_tien()} $")

    def so_sanh_gia(self, temp):
        if self.__don_gia < temp.__don_gia:
            return f"{self.__ten_hang} có giá thấp hơn {temp.__ten_hang}"
        elif self.__don_gia > temp.__don_gia:
            return f"{self.__ten_hang} có giá cao hơn {temp.__ten_hang}"
        else:
            return f"{self.__ten_hang} và {temp.__ten_hang} có giá bằng nhau"


# Ví dụ sử dụng:
hang_hoa1 = HangHoa("MH01", "Táo", 1000, 6)
hang_hoa2 = HangHoa("MH02", "Thanh Long", 2000, 4)

print("Thông tin hàng hóa 1:")
hang_hoa1.hien_thi_thong_tin()

print("\nThông tin hàng hóa 2:")
hang_hoa2.hien_thi_thong_tin()

print("\nKết quả so sánh giá:")
print(hang_hoa1.so_sanh_gia(hang_hoa2))
