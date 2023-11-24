my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

number_even_list = [num for num in my_list if num%2==0]

print(number_even_list)

number_odd_list = [num for num in my_list if num%2!=0]
print(number_odd_list)