def mua_ve(s, danh_sach_ve):
    so_nguoi_mua_ve = 0

    for so_ve in danh_sach_ve:
        # Kiểm tra số ghế trống còn lại
        if s >= so_ve:
            s -= so_ve
            so_nguoi_mua_ve += 1
        else:
            # Nếu số ghế trống còn lại ít hơn hoặc bằng 3, tuyên bố hết chỗ và dừng bán vé
            if s <= 3:
                print("Hết chỗ!")
                break
            else:
                print("Khách hàng tiếp theo, không đủ chỗ cho số vé bạn muốn mua.")
                break

    return so_nguoi_mua_ve, s

# Ví dụ sử dụng hàm
so_cho_trong_ban_dau = 10
danh_sach_ve_muon_mua = [3, 2, 4, 1]

so_nguoi_mua, so_cho_trong_con_lai = mua_ve(so_cho_trong_ban_dau, danh_sach_ve_muon_mua)

print(f"Số người mua vé: {so_nguoi_mua}")
print(f"Số chỗ trống còn lại: {so_cho_trong_con_lai}")
