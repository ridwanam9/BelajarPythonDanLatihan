# Hitung Huruf Vokal
# Buat fungsi count_vowels(text) yang menerima string, dan mengembalikan jumlah huruf vokal (a, i, u, e, o) di dalam string.

def count_vowels(words):

    lower = words.lower()

    print(lower)
    vokals = "aiueo"
    count = 0
    for x in lower:
        if x in vokals:
            count += 1
    return count



# print(count_vowels("halo dunia"))
print(count_vowels("hAlo dunia"))

