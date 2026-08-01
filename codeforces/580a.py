n = int(input())
a = list(map(int, input().split()))

# count = 0
# max_numbers = []
# for i in range(1, n):
#     if a[i] < a[i-1]:
#         max_numbers.append(count)
#         count = 0
#     else:
#         count += 1
# print(max_numbers)
# print(max(max_numbers)+1)

count = 0
max_numbers = 0
for i in range(n-1):
    if a[i] <= a[i+1]:
        count += 1
        if count > max_numbers:
            max_numbers = count
    else:
        if count > max_numbers:
            max_numbers = count
        count = 0
    # print(count, max_numbers)


# print(max_numbers)
print(max_numbers+1)