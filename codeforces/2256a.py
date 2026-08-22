t = int(input())
for _ in range(t):
    arr = sorted(list(map(int, input().split())))
    # print(arr)
    if arr[0]+arr[1] < arr[2]:
        arr.pop()
        arr.append(arr[0]+arr[1])
    print(max(arr)-min(arr))
    

