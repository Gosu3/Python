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
    

