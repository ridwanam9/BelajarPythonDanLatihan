
# import itertools
# result = itertools.permutations(height, 2)
# # print(result) # Output: [('g', 'e'), ('g', 'k'), ('e', 'g'), ('e', 'k'), ('k', 'g'), ('k', 'e')]
# print(list(result)) # Output: [('g', 'e'), ('g', 'k'), ('e', 'g'), ('e', 'k'), ('k', 'g'), ('k', 'e')]

# height = [1,8,6,2,5,4,8,3,7]

# max_area = 0
# for i in range(len(height)):
#     steps = 0
#     for j in range(i, len(height)):
#         # print(f"{[height[i], height[j], steps]}")
#         area = (min(height[i], height[j]))*steps
#         if area > max_area:
#             max_area = area
#         steps += 1
        

# print(max_area)
# # return max_area


class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            h = min(height[left], height[right])
            width = right - left
            area = h * width

            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
    

    # print(maxArea([1,8,6,2,5,4,8,3,7]))

# input
height = [1,8,6,2,5,4,8,3,7]

# membuat object
sol = Solution()

# menjalankan function
result = sol.maxArea(height)

print(result)