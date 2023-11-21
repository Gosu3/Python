import math
sequence = []
def input_sequence():
    print("Bạn chọn option 1")
    global sequence
    try:
        sequence = [int(x) for x in input("Nhập dãy số, cách nhau bằng dấu cách: ").split()]
    except ValueError:
        print("Lỗi! Hãy đảm bảo bạn chỉ nhập các số nguyên.")

def sum_sequence():
    print("Bạn chọn option 2")
    global sequence
    return sum(sequence)


def sochinhphuong():
    print("Bạn chọn option 3")
    global sequence
    soChinhphuong = [num for num in sequence if math.isqrt(num)**2 == num]
    print("Các số chính phương trong dãy số là: ", soChinhphuong)
    
def even_numbers():
    print("Bạn chọn option 4")
    global sequence
    even_num = [num for num in sequence if num % 2 == 0]
    print("Các sô chẵn trong dãy số là: ", even_num)
    
def print_sequence():
    print("Bạn chọn option 5")
    global sequence
    print("Dãy số: ", sequence)
    
def sapxep_sequence():
    print("Bạn chọn option 6")
    global sequence
    sorted_sequence = sorted(sequence)
    print("Dãy số sau khi sắp xếp là: ", sorted_sequence)

    
def display_menu():
    print(""""Menu
    
    1. Nhập dãy số
    2. Tính tổng dãy số
    3. In ra các số chính phương
    4. In ra các số chẵn
    5. In dãy số
    6. Sắp xếp dãy số
    7. Thoát""")
    
    
    
#main
while True:
    display_menu()
    choice = input ("Bạn hãy lựa chọn từ 1-7: ")
    
    if choice == '1':
        input_sequence()
    elif choice == '2':
        sum_sequence()
        total = sum_sequence()
        print("Tổng dãy số: ", total)
    elif choice == '3':
        sochinhphuong()
    elif choice == '4':
        even_numbers()
    elif choice == '5':
        print_sequence()
    elif choice == '6': 
        sapxep_sequence()
    elif choice == '7':
        break
    else:
        print("Lựa chọn không hợp lệ. Hãy nhập số từ 1 đến 7.")
        
        
