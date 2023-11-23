input_string = input("Nhập vào 1 chuỗi: ")


#Chuẩn hóa chuỗi: Xét tất cả các ký tự trong chuỗi (trừ vị trí đầu) 
# - nếu là chữ hoa thì đổi thành chữ thường
# - Đổi chữ cái đầu thành chữ in hoa



#Loại bỏ dấu trắng thừa
clean_str = input_string.strip()

#chuyển đổi tất cả ký tự thành chữ thường
lower_str = clean_str.lower()

# chuyển đổi ký tự đầu thành chữ in hoa
if lower_str:
    normal_str = lower_str[0].upper() + lower_str[1:] #cộng xâu ký tự
else:
    normal_str =""
    
print(normal_str)



#Solution cho phần xử lý dấu câu
