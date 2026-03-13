
# import itertools
# result = itertools.permutations(height, 2)
# # print(result) # Output: [('g', 'e'), ('g', 'k'), ('e', 'g'), ('e', 'k'), ('k', 'g'), ('k', 'e')]
# print(list(result)) # Output: [('g', 'e'), ('g', 'k'), ('e', 'g'), ('e', 'k'), ('k', 'g'), ('k', 'e')]

height = [1,8,6,2,5,4,8,3,7]

max_area = 0
for i in range(len(height)):
    steps = 0
    for j in range(i, len(height)):
        # print(f"{[height[i], height[j], steps]}")
        area = (min(height[i], height[j]))*steps
        if area > max_area:
            max_area = area
        steps += 1
        

print(max_area)
# return max_area


