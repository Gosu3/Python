class Person:
    def __init__(self, họ_tên, ngày_sinh, giới_tính, địa_chỉ):
        self.__họ_tên = họ_tên
        self.__ngày_sinh = ngày_sinh
        self.__giới_tính = giới_tính
        self.__địa_chỉ = địa_chỉ

    @property
    def hoten(self):
        return self.__họ_tên
    @property
    def ngaysinh(self):
        return self.__ngày_sinh
    @property
    def gioitinh(self):
        return self.__giới_tính
    @property
    def diachi(self):
        return self.__địa_chỉ
    def nhập(self):
        self.__họ_tên = input("Nhập Họ tên: ")
        self.__ngày_sinh = input("Nhập Ngày sinh: ")
        self.__giới_tính = input("Nhập Giới tính: ")
        self.__địa_chỉ = input("Nhập địa chỉ: ")

    def hiển_thị(self):
        print(f"Họ tên: {self.__họ_tên}")
        print(f"Ngày sinh: {self.__ngày_sinh}")
        print(f"Giới tính: {self.__giới_tính}")
        print(f"Địa chỉ: {self.__địa_chỉ}")

class Student(Person):
    def __init__(self, họ_tên, ngày_sinh, giới_tính, địa_chỉ, mã_sinh_viên, điểm_trung_bình, email):
        super().__init__(họ_tên, ngày_sinh, giới_tính, địa_chỉ)
        self.__mã_sinh_viên = mã_sinh_viên
        self.__điểm_trung_bình = điểm_trung_bình
        self.__email = email

    def nhập(self):
        super().nhập()
        self.__mã_sinh_viên = input("Nhập Mã sinh viên (8 kí tự): ")
        self.__điểm_trung_bình = float(input("Nhập Điểm trung bình (0.0 - 10.0): "))
        self.__email = input("Nhập Email: ")

        # Kiểm tra điều kiện Email
        while "@" not in self.__email or " " not in self.__email:
            print("Email không hợp lệ. Email phải chứa kí tự @ và tồn tại khoảng trắng.")
            self.__email = input("Nhập Email: ")

    def hiển_thị(self):
        super().hiển_thị()
        print(f"Mã sinh viên: {self.__mã_sinh_viên}")
        print(f"Điểm trung bình: {self.__điểm_trung_bình}")
        print(f"Email: {self.__email}")

    def có_học_bổng(self):
        return self.__điểm_trung_bình >= 8.0



if __name__ == "__main__":
    student = Student("", "", "", "", "", 0.0,"" )
    student.nhập()
    student.hiển_thị()

    if student.có_học_bổng():
        print("Sinh viên này được học bổng.")
    else:
        print("Sinh viên này không được học bổng.")

