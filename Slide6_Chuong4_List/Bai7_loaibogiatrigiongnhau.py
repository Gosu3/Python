my_list = ['abc', 'xyz', 'abc', '12', 'ii', '12','5a']


seen_element = []
result_list = []

for item in my_list:
    if item not in seen_element:
        seen_element.append(item)
        result_list.append(item)
    else:
        result_list.remove(item)
        
print(result_list)