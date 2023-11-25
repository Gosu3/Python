inventory = {
        'gold': 500    
    
}

new_key = 'key4'
new_value = 'value4'

inventory[new_key]= new_value


print(inventory)


#khai báo 1 từ điển mới gồm giá trị key:value
#sử dụng 
# my_dict.update(new_items)


#sắp xếp item của key trong từ điển

target_key = 'value3'

sort_values = sorted(inventory[target_key])


sort_dict = {target_key:sort_values, **{key:value for key,value in inventory.items() if key != target_key}}
print(sort_dict)