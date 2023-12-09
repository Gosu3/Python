def them_phan_tu(arr, vi_tri, gia_tri):
    arr.insert(vi_tri, gia_tri)

def main():
    danh_sach = [1, 2, 3, 4, 5]

    print("Danh sách ban đầu:", danh_sach)

    vi_tri_can_them = int(input("Nhập vào vị trí cần thêm: "))
    gia_tri_can_them = int(input("Nhập vào giá trị cần thêm: "))

    them_phan_tu(danh_sach, vi_tri_can_them, gia_tri_can_them)

    print("Danh sách sau khi thêm:", danh_sach)

if __name__ == "__main__":
    main()
