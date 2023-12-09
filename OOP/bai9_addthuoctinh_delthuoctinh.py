class Sinhvien:
    student_id = "MS10"
    student_name = "Nguyễn Văn Bờ"
    
print("Sinh viên khi chưa được thêm: ")

for attr,value in Sinhvien.__dict__.items():
    if not attr.startswith('_'):
        print(f"{attr} -> {value}")
        
print("\nSau khi thêm student_class: ")

Sinhvien.student_class = '12A1'

for attr, value in Sinhvien.__dict__.items():
    if not attr.startswith('_'):
        print(f"{attr} -> {value}")
        
        
print("\nSau khi loại bỏ student_name: ")

del Sinhvien.student_name

for attr, value in Sinhvien.__dict__.items():
    if not attr.startswith('_'):
        print(f"{attr} -> {value}")