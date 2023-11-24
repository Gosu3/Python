def filter_words_by_length(words, length):
    filtered_words = [word for word in words if len(word) > length]
    return filtered_words


n = int(input("Nhập số nguyên n: "))


word_list = input("Nhập danh sách từ (phân tách bởi dấu phẩy): ").split(',')


word_list = [word.strip() for word in word_list]


# Tìm các từ có độ dài lớn hơn n
result_words = filter_words_by_length(word_list, n)

# In kết quả
print(f"Các từ có độ dài lớn hơn {n} là: {result_words}")
