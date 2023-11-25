def tinh_diem_trung_binh(danh_sach_hoc_vien):
    diem_tb_hoc_vien = {}

    for hoc_vien, diem in danh_sach_hoc_vien.items():
        # Kiểm tra xem danh sách điểm có rỗng không
        if diem:
            diem_tb = sum(diem) / len(diem)
            diem_tb_hoc_vien[hoc_vien] = diem_tb
        else:
            diem_tb_hoc_vien[hoc_vien] = "Không có điểm"

    return diem_tb_hoc_vien

# Ví dụ sử dụng hàm
danh_sach_diem = {
    'HocVien1': [8, 7, 9],
    'HocVien2': [6, 5, 7],
    'HocVien3': [9, 8, 10],
    'HocVien4': []
}

ket_qua = tinh_diem_trung_binh(danh_sach_diem)

# In kết quả
for hoc_vien, diem_tb in ket_qua.items():
    print(f"{hoc_vien}: {diem_tb}")
    
############
def in_diem_trung_binh_theo_ten(hoc_vien, danh_sach_hoc_vien):
    # Kiểm tra xem tên học viên có trong danh sách không
    if hoc_vien in danh_sach_hoc_vien:
        diem = danh_sach_hoc_vien[hoc_vien]

        # Kiểm tra xem danh sách điểm có rỗng không
        if diem:
            diem_tb = sum(diem) / len(diem)
            print(f"Điểm trung bình của học viên {hoc_vien}: {diem_tb}")
        else:
            print(f"Học viên {hoc_vien} không có điểm.")
    else:
        print(f"Học viên {hoc_vien} không có trong danh sách.")

# Ví dụ sử dụng hàm
danh_sach_diem = {
    'HocVien1': [8, 7, 9],
    'HocVien2': [6, 5, 7],
    'HocVien3': [9, 8, 10],
}

ten_hoc_vien_can_tim = 'HocVien2'
in_diem_trung_binh_theo_ten(ten_hoc_vien_can_tim, danh_sach_diem)


