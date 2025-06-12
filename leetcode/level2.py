# 4. Cari Nilai Maksimum dalam List

def find_max(nums):

    maximum = max(nums)
    print(f"Nilai maximal = {maximum}")

input_nums = [4,3,14,8,20,17,19,34]
find_max(input_nums)


# 5. Filter Angka Genap
def filter_even(nums):

    evens = [x for x in nums if x % 2 == 0 ]
    print(evens)

input_nums = [4,3,14,8,20,17,19,34]
filter_even(input_nums)


# 6. Hitung Frekuensi Karakter
def char_count(s):

    thisdict = {}
    for x in s.lower():
        count = s.lower().count(x)
        thisdict[f"{x}"] = count

    print(thisdict)

char_count("RidwanAmirulMaulana")