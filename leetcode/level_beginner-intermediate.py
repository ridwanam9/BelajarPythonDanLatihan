# 1: Angka Unik
# Deskripsi:
# Buat fungsi find_unique(nums) yang menerima list angka, lalu mengembalikan list baru berisi hanya angka-angka yang muncul sekali saja.

def find_unique(nums):
    # your code here
    return [x for x in nums if nums.count(x) == 1]

print(find_unique([2,3,3,4,5,5,6,6,7,8,9]))

# 2: Hitung Kata
# Deskripsi:
# Buat fungsi word_count(text) yang menerima string kalimat dan mengembalikan jumlah kata di dalamnya.

# Contoh: "Aku sedang belajar Python"
# Output: 4

def word_count(text):

    list_txt = text.split()
    return len(list_txt)

print(word_count("Aku sedang belajar Python"))


# 3: Bilangan Prima
# Deskripsi:
# Buat fungsi is_prime(n) yang mengembalikan True jika n adalah bilangan prima, False jika bukan.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):  # Cek sampai akar n lebih efisien
        if n % i == 0:
            return False
    return True

print(is_prime(9))   # False
print(is_prime(8))   # False
print(is_prime(17))  # True


# 4. Ubah Huruf ke Angka (Ordinal)
# Deskripsi:
# Buat fungsi char_to_num(s) yang menerima string dan mengubah setiap huruf menjadi angka berdasarkan urutan alfabetnya (a=1, b=2, ..., z=26). Abaikan spasi dan tanda baca.

# Contoh: "abc" -> [1, 2, 3]
#         "halo" -> [8, 1, 12, 15]

def char_to_num(s):

    # # cara panjang
    # chars = list(map(chr, range(97, 123)))

    # list_s = []
    # for x in s:
    #     x_kecil = x.lower()
    #     list_s.append(x_kecil)

    # angka = []
    # for x in range(len(list_s)):
    #     for y in range(len(chars)):
    #         if chars[y] == list_s[x]:
    #             angka.append(y + 1)
                
    # return angka

    # # cara pendek
    return [ord(c.lower()) - 96 for c in s if c.isalpha()]


print(char_to_num("abc"))
print(char_to_num("halo"))
print(char_to_num("Halo"))


# 5. Group Anagram
# Deskripsi (lebih menantang):
# Buat fungsi group_anagrams(words) yang mengelompokkan kata-kata yang merupakan anagram ke dalam list yang sama.

# Contoh:
# Input: ["aku", "kua", "kamu", "mauk", "satu", "taus"]
# Output: [['aku', 'kua'], ['kamu', 'mauk'], ['satu', 'taus']]

from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word.lower()))
        groups[key].append(word)
    
    return list(groups.values())

print(group_anagrams(["aku", "kua", "kamu", "mauk", "satu", "taus", "anagram", "anabul"]))