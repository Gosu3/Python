import math

class vecto:
    def __init__(self, x1,y1,x2,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        
    def hien_thi_thong_tin(self):
        print(f" Tọa độ điểm đầu là: ({self.x1}, {self.y1})")
        print(f" Tọa độ điểm cuối là: ({self.x2}, {self.y2})")
        
    def kiem_tra_bang_nhau (self, other):
        
        return vecto(self.x1, self.y1, other.x2, other.y2)
        
    
    
    def module_2vecto(self):
        x21 = self.x2 - self.x1
        y21 = self.y2 - self.y1
        
        return math.sqrt(x21**2 + y21**2)
    
    def cung_phuong(self, solve):
        h1 = self.x2 - self.x1
        t1 = self.y2 - self.y1
        h2 = solve.x2 - solve.x1
        t2 = solve.y2 - solve.y1
        
        return h1*t2  == h2*t1
    
    def cong(self,other):
        hoanh_do = self.x2 + other.x2
        tung_do = self.y2 + other.y2
        
        return vecto(self.x2, self.y2, hoanh_do, tung_do)
    def tru(self, other):
        hoanh_do = self.x2 - other.x2
        tung_do = self.y2 - other.y2
        return vecto(self.x2, self.y2, hoanh_do, tung_do)
    
    def nhan(self, scalar):
        hoanh_do = self.x2 * scalar
        tung_do = self.y2 * scalar
        
        return vecto(self.x2,self.y2, hoanh_do, tung_do)
    

# Ví dụ sử dụng:
vecto1 = vecto(1, 2, 3, 4)
vecto2 = vecto(5, 6, 7, 8)

print("Thông tin Vecto 1:")
vecto1.hien_thi_thong_tin()

print("\nThông tin Vecto 2:")
vecto2.hien_thi_thong_tin()

tong_vecto = vecto1.cong(vecto2)
print("\nTổng hai Vecto:")
tong_vecto.hien_thi_thong_tin()

hieu_vecto = vecto1.tru(vecto2)
print("\nHiệu hai Vecto:")
hieu_vecto.hien_thi_thong_tin()

scalar = 2
nhan_scalar_vecto1 = vecto1.nhan(scalar)
print(f"\nNhân Vecto 1 với scalar {scalar}:")
nhan_scalar_vecto1.hien_thi_thong_tin()


    
        
    
    

    
        
        
        
        