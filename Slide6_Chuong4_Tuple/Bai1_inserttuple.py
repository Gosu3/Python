my_tuple = ('a', 'b', 'd', 'e')

convert_list = list(my_tuple)

convert_list.insert(2, 'c')

switch_tuple = tuple(convert_list)

print(switch_tuple)

