def main():
    # Nhập vào danh sách các số nguyên nhỏ hơn 10
    numbers = []
    while len(numbers) < 10:
        try:
            number = int(input("Nhập số nguyên nhỏ hơn 10: "))
            if 0 <= number < 10:
                numbers.append(number)
            else:
                print("Vui lòng nhập số nguyên nhỏ hơn 10.")
        except ValueError:
            print("Vui lòng nhập số nguyên.")

    # Sắp xếp danh sách theo chiều giảm dần
    numbers.sort(reverse=True)

    # In danh sách đã sắp xếp
    print("Danh sách số đã sắp xếp theo chiều giảm dần:", numbers)

    # In ra các số chia hết cho 3 có tận cùng là 8
    divisible_by_3_ending_with_8 = [num for num in numbers if num % 3 == 0 and num % 10 == 8]
    print("Các số chia hết cho 3 có tận cùng là 8:", divisible_by_3_ending_with_8)

    # In ra các số chia hết cho 7 trong danh sách
    divisible_by_7 = [num for num in numbers if num % 7 == 0]
    print("Các số chia hết cho 7 trong danh sách:", divisible_by_7)

if __name__ == "__main__":
    main()
