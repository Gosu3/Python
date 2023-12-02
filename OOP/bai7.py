class Xe:
    def __init__(self, nhan_hieu, toc_do):
        self.__nhan_hieu = nhan_hieu
        self.__toc_do = toc_do
#Cách 1 sử dụng property
    @property
    def toc_do(self):
        return self.__toc_do
    
# Cách 2 sử dụng set/get
    def get_toc_do(self):
        return self.__toc_do
    
    def hien_thi_xe (self):
        print(f"Nhãn hiệu: {self.__nhan_hieu}")
        print(f"Tốc độ: {self.__toc_do}")
        
        
class Congdan:
    def __init__(self, ho_dem, ten, tuoi):
        self.__ho_dem = ho_dem
        self.__ten = ten
        self.__tuoi = tuoi
        
    def hien_thi_cong_dan(self):
        print(f"Họ đệm: {self.__ho_dem}")
        print(f"Tên: {self.__ten}")
        print(f"Tuổi: {self.__tuoi}")
        
    def kiem_tra_dieu_kien_lai_xe(self,xe):
        if self.__tuoi < 18:
            print("Công dân không được phép lái xe")
        else:
            if self.__tuoi < 50:
                print("Công dân được phép lái xe")
            else:
                if(xe.toc_do < 150):  #sử dụng xe.get_toc_do() nếu dùng cách 2
                    print("Công dân được phép lái xe")
                else:
                    print("Công dân không được phép lái xe >=150 phân khối")


    
cong_dan = Congdan("Nguyen", "Van Tho", 51)
xe = Xe("Honda", 180)


print("Thông tin công dân: ")
cong_dan.hien_thi_cong_dan()

print("Thông tin xe: ")
xe.hien_thi_xe()

cong_dan.kiem_tra_dieu_kien_lai_xe(xe)