n, k = map(int, input().split())
arr = list(map(int, input().split()))
# print(f"{arr[k-1]}")
# Jika semua score adalah 0
if arr[0] == 0:
    print(0)
elif arr[k-1] != 0:
    count = 0   
    for x in arr:
        if x >= arr[k-1]:
            count += 1
    print(count)


# Not Finished