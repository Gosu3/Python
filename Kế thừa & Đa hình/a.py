def xoa_phan_tu(arr, vi_tri):
    try:
        arr.pop(vi_tri)
        return True
    except IndexError:
        print("Vị trí không hợp lệ. Vui lòng nhập lại.")
        return False

def main():
    danh_sach = [1, 2, 3, 4, 5]

    print("Danh sách ban đầu:", danh_sach)

    vi_tri_can_xoa = int(input("Nhập vào vị trí cần xóa: "))

    if xoa_phan_tu(danh_sach, vi_tri_can_xoa):
        print("Danh sách sau khi xóa:", danh_sach)



if __name__ == "__main__":
    main()
