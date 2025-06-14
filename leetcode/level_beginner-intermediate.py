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

    if n == 0 or n == 1:
        return True
    elif n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                return False
            else:
                return True

print(is_prime(9))
print(is_prime(8))
print(is_prime(17))

# 4. Ubah Huruf ke Angka (Ordinal)
# Deskripsi:
# Buat fungsi char_to_num(s) yang menerima string dan mengubah setiap huruf menjadi angka berdasarkan urutan alfabetnya (a=1, b=2, ..., z=26). Abaikan spasi dan tanda baca.

# Contoh: "abc" -> [1, 2, 3]
#         "halo" -> [8, 1, 12, 15]

def char_to_num(s):
    
    chars = list(map(chr, range(97, 123)))

    list_s = []
    for x in s:
        x_kecil = x.lower()
        list_s.append(x_kecil)

    angka = []
    for x in range(len(list_s)):
        for y in range(len(chars)):
            if chars[y] == list_s[x]:
                angka.append(y + 1)
                
    return angka


print(char_to_num("abc"))
print(char_to_num("halo"))
print(char_to_num("Halo"))


# 5. Group Anagram
# Deskripsi (lebih menantang):
# Buat fungsi group_anagrams(words) yang mengelompokkan kata-kata yang merupakan anagram ke dalam list yang sama.

# Contoh:
# Input: ["aku", "kua", "kamu", "mauk", "satu", "taus"]
# Output: [['aku', 'kua'], ['kamu', 'mauk'], ['satu', 'taus']]

def group_anagrams(words):

    list_combined = []
    
    for x in words:
        for y in words[1:]:
            if x.lower() != y.lower():
                if sorted(x.lower()) == sorted(y.lower()):
                    list_combined.append([x, y])
                    # if [x, y] == [y, x] in list_combined:
                    #     list_combined.remove([y, x])
          

    # for x in range(len(words)):
    #     words[x].sort()
    #     for y in range(1, len(words)):
    #         words[y].sort()
    #         if words[x] == words[y]:
    #             list_combined.append([words[x], words[y]])

    # list_set = list(set(list_combined))
    return list_combined


    # sorted(s1.lower()) == sorted(s2.lower())

print(group_anagrams(["aku", "kua", "kamu", "mauk", "satu", "taus", "anagram", "anabul"]))