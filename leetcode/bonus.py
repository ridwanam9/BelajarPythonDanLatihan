# 10. Two Sum (LeetCode-style)
# Diberikan list nums dan target target, kembalikan indeks dua angka yang jika dijumlahkan hasilnya target.

def two_sum(nums, target):
    
    for x in nums:
        for y in nums:
            if x + y == target:
                hasil = print(f"[{nums.index(x)}, {nums.index(y)}]")
                return hasil

list_angka = [1,2,3,8,9,20,46]
two_sum(list_angka, 5)
two_sum(list_angka, 17)
