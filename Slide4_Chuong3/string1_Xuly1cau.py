input_string = input("Nhập vào chuỗi: ")

#Loại bỏ dấu trắng thừa
words = input_string.split()

print(words)
#Đếm số từ

word_count = len(words)

print("Số từ trong chuỗi là: ", word_count)


print("Các từ trong chuỗi là: ")

for word in words:
    print(word)
