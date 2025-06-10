# 1. Buat fungsi odd_or_even(n) yang mengembalikan 'Ganjil' jika n ganjil dan 'Genap' jika n genap.

def odd_or_even(n):
    # your code here
    if n % 2 == 1:
        print("Angka adalah Ganjil")
    elif n % 2 == 0:
        print("Angka adalah Genap")

odd_or_even(4)

odd_or_even(7)

print("-"*30)
# 2. Buat fungsi sum_to_n(n) yang menjumlahkan angka dari 1 sampai n.
def sum_to_n(n):
    return sum(range(1, n + 1))

n = 6
result = sum_to_n(n)
print(f"The sum of numbers from 1 to {n} is: {result}")


print("-"*30)
# 3. Buat fungsi reverse_string(s) yang menerima string s dan mengembalikan kebalikannya.

def reverse_string(s):
    # your code here
    print(s[::-1])

reverse_string("Ridwan Amirul Maulana")