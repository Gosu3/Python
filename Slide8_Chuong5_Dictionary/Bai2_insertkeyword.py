inventory = {
        'gold': 500,
        'pouch' : ['flint', 'twine', 'gemstone'],
        'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

new_key = 'pocket'
new_value = '[seashell, strange berry, lint]'

inventory[new_key]= new_value

print("Từ điển sau khi được thêm: ")
print(inventory)
print()


#khai báo 1 từ điển mới gồm giá trị key:value
#sử dụng 
# my_dict.update(new_items)


#sắp xếp item của key trong từ điển

target_key = 'backpack' 

sort_values = sorted(inventory[target_key])


sort_dict = {target_key:sort_values, **{key:value for key,value in inventory.items() if key != target_key}}
print("Từ điển sau khi được sắp xếp: ")
print(sort_dict)