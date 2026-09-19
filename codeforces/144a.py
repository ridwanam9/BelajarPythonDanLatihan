n = int(input())
arr = list(map(int, input().split()))

if arr[0] == max(arr) and arr[-1] == min(arr):
    print(0)
elif arr[0] == max(arr) and arr[-1] != min(arr):
    min_num = 101
    i_min_num = 0
    for i in range(n):
        if arr[i] <= min_num:
            min_num = arr[i]
            i_min_num = i
    steps_min = (n - i_min_num) - 1
    print(steps_min)

elif arr[0] != max(arr) and arr[-1] == min(arr):
    max_num = 0
    i_max_num = 0
    for i in range(n):
        if arr[i] > max_num:
            max_num = arr[i]
            i_max_num = i
    steps_max = n - (n - i_max_num)
    print(steps_max)
    
else:
    min_num = 101
    i_min_num = 0
    max_num = 0
    i_max_num = 0
    for i in range(n):
        if arr[i] > max_num:
            max_num = arr[i]
            i_max_num = i
        if arr[i] <= min_num:
            min_num = arr[i]
            i_min_num = i

    steps_max = n - (n - i_max_num)
    steps_min = (n - i_min_num) - 1
    if i_min_num < i_max_num:
        print(steps_min + steps_max - 1)
    else:
        print(steps_min + steps_max)

# print(f"index max {i_max_num}")
# print(f"index min {i_min_num}")
# print(steps_max)
# print(steps_min)


# print(max_num)
# print(min_num)
    
    

