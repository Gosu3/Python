def factorial(n):
    """Hàm tính giai thừa của n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def combination(n, k):
    """Hàm tính giá trị tổ hợp chập k của n."""
    if k < 0 or k > n:
        return 0
    else:
        return factorial(n) // (factorial(k) * factorial(n - k))

# Sử dụng hàm để tính giá trị tổ hợp chập k của n
n_value = 5
k_value = 2

result = combination(n_value, k_value)

print(f"Tổ hợp chập {k_value} của {n_value} là: {result}")
