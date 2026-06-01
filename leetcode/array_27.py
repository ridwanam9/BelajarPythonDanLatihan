# Removes Element

def remove_duplicate(nums, val):

    if not nums:
        return 0

    i = 0
    # arr = []
    for j in range(1, len(nums)):
        if nums[j] != val:
            i += 1
            # arr.append(nums[j])
            nums[i] = nums[j]

    return i + 1


print(remove_duplicate([3,2,2,3], 3)) # 2
print(remove_duplicate([0,1,2,2,3,0,4,2], 2)) # 5