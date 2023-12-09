def tim_kiem_phan_tu(arr, gia_tri):
    return gia_tri in arr

def main():
    danh_sach = [1, 2, 3, 4, 5]

    gia_tri_can_tim = int(input("Nhập giá trị cần tìm: "))

    if tim_kiem_phan_tu(danh_sach, gia_tri_can_tim):
        print(f"Giá trị {gia_tri_can_tim} được tìm thấy trong danh sách.")
    else:
        print(f"Giá trị {gia_tri_can_tim} không có trong danh sách.")

if __name__ == "__main__":
    main()
