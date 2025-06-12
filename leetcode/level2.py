# 4. Cari Nilai Maksimum dalam List

def find_max(nums):
    return max(nums)

print(find_max([4,3,14,8,20,17,19,34]))

# 5. Filter Angka Genap
def filter_even(nums):
    return [x for x in nums if x % 2 == 0]

print(filter_even([4,3,14,8,20,17,19,34]))



# 6. Hitung Frekuensi Karakter
def char_count(s):
    result = {}
    for char in s.lower():
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

print(char_count("RidwanAmirulMaulana"))
