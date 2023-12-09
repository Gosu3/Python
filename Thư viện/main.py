import numpy as np

def thong_tin_mang(arr):
    sum_arr = np.sum(arr)
    mean_arr = np.mean(arr)
    max_arr = np.max(arr)
    min_arr = np.min(arr)

    return sum_arr, mean_arr, max_arr, min_arr

def giatri_array():
    # n = int(input("Nhập vào kích thước mảng n: "))
    # random_arr = np.random.randint(0, 101,n)


    # print("Mảng ngẫu nhiên:")
    # print(random_arr)

    sum_arr = thong_tin_mang(random_arr)
    mean_arr = thong_tin_mang(random_arr)
    max_arr = thong_tin_mang(random_arr)
    min_arr = thong_tin_mang(random_arr)

    print(f"\nTổng giá trị các phần tử trong mảng: {sum_arr}")
    print(f"Trung bình giá trị các phần tử trong mảng: {mean_arr}")
    print(f"Giá trị lớn nhất trong mảng: {max_arr}")
    print(f"Giá trị nhỏ nhất trong mảng: {min_arr}")
    


    

def main_delete_array(arr):
    vitri = int(input("Nhập vào vị trí cần xóa: "))
    arr1 = arr.delete(vitri)
    print("Mảng sau khi thực hiện xóa", arr1)
    
    
def main_insert_array():

    add_vitri = int(input("Nhập vào vị trí cần thêm: "))
    add_giatri = int(input("Nhập vào giá trị cần thêm: "))

    add_phan_tu(random_arr, add_vitri, add_giatri)

    print("Danh sách sau khi thêm:", random_arr)
    


if __name__ == "__main__":
    n = int(input("Nhập vào kích thước mảng n: "))
    random_arr = np.random.randint(0, 101,n)


    print("Mảng ngẫu nhiên:")
    print(random_arr)
    # giatri_array()
    
    
    # main_insert_array()
    main_delete_array(random_arr)

