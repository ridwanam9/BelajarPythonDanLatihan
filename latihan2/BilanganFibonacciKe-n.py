# Bilangan Fibonacci ke-n
# Buat fungsi fibonacci(n) yang mengembalikan angka ke-n dari deret Fibonacci.

def fibonacci(n):
    a, b = 0, 1
    next = b
    fibo_list = []

    for x in range(n):
        fibo_list.append(next)
        # print(next, end=" ")
        next = a + b
        a, b = b, next
        x += 1

    print(fibo_list[n-1])

fibonacci(7)
# Output: 13