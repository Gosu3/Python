def tinh_tong_so_tien_ca_lam_viec(danh_sach_so_tien):
    tong_so_tien = 0

    for so_tien in danh_sach_so_tien:
        # Kiểm tra xem số tiền có phải là số dương không
        if so_tien > 0:
            tong_so_tien += so_tien

    return tong_so_tien

# Ví dụ sử dụng hàm
danh_sach_so_tien_ca_1 = [50.0, -10.0, 30.0, 0.0, 20.0]
tong_so_tien_ca_1 = tinh_tong_so_tien_ca_lam_viec(danh_sach_so_tien_ca_1)

print(f"Tổng số tiền thu ngân đã thu trong ca làm việc: {tong_so_tien_ca_1} đồng")
