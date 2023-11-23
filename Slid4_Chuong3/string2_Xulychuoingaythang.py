from datetime import date

today = date.today()
input_date = input("Nhập chuỗi ngày tháng (dd/mm/yyyy): ")


#Xóa dấu trắng thừa

cleaned_space = input_date.split("/")
print(cleaned_space)

if len(cleaned_space)!=3:
    print("Không phải ngày tháng")
    
else: 
    
    d = int(cleaned_space[0])
    m = int(cleaned_space[1])
    y = int(cleaned_space[2])
    
    if(y<1900 or y > today.year):
        print("Không phải ngày tháng")
    else:
        if m in (1,3,5,7,8,10,12) and (d>0 and d<=31): 
            print("Đúng là ngày tháng")       
        elif m in(4,6,9,11) and (d>0 and d<=30):
            print("Đúng là ngày tháng")
        elif m ==2 and y%400 ==0 or (y%4==0 and y%100!=0) and (d>0 and d<=29):
            print("Đúng là ngày tháng")
        elif m == 2 and (d>0 and d<=28):
            print("Đúng là ngày tháng")
            
        else:
            print("Không phải ngày tháng")
            