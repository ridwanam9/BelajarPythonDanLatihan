def threeSumClosest(nums, target):
    nums.sort()
    result = {}
    closest = 0
    distance = 1
    smallest_distance = 10

    for i in range(len(nums)):
        # skip duplicate
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == target:
                return total

            if total > target:
                distance = total - target
                if distance < smallest_distance:
                    smallest_distance = distance
                # # skip duplicate
                # while left < right and nums[left] == nums[left + 1]:
                #     left += 1
                # while left < right and nums[right] == nums[right - 1]:
                #     right -= 1

                # left += 1
                # right -= 1


            elif total < target:
                distance = target - total
                if distance < smallest_distance:    
                    smallest_distance = distance
                # # skip duplicate
                # while left < right and nums[left] == nums[left + 1]:
                #     left += 1
                # while left < right and nums[right] == nums[right - 1]:
                #     right -= 1

                # left += 1
                # right -= 1



    return smallest_distance

nums = [[-1,2,1,-4]]
print(threeSumClosest(nums, 1))