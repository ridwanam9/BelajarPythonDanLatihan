t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    if arr.count(0) <= 1:
        print(-1)
    elif arr[0] == 0 and arr[-1] == 0:
        print(0)
    