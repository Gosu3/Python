input_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')
input_list = list(input_tuple)
seen_elements = []
result_list = []

for item in input_tuple:
    if item not in seen_elements:
        seen_elements.append(item)
        result_list.append(item)
    else:
        result_list.remove(item)
        
result_tuple = tuple(result_list)
print(result_tuple)