def mua_ve(s, danh_sach_ve):
    so_nguoi_mua_ve = 0

    for so_ve in danh_sach_ve:

        if s >= so_ve:
            s -= so_ve
            so_nguoi_mua_ve += 1
        else:
            if s <= 3:
                print("Hết chỗ!")
                break
            else:
                print("Khách hàng tiếp theo, không đủ chỗ cho số vé bạn muốn mua.")
                break

    return so_nguoi_mua_ve, s
so_cho_trong_ban_dau = int(input("Nhập số chỗ trống ban đầu: ")
so_nguoi_mua, so_cho_trong_con_lai = mua_ve(so_cho_trong_ban_dau, danh_sach_ve_muon_mua)

print("Số người mua vé: {so_nguoi_mua}")
print(f"Số chỗ trống còn lại: {so_cho_trong_con_lai}")
