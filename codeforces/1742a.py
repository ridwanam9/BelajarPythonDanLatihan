t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    arr = [a, b, c]
    d = sorted(arr)
    if d[0] + d[1] == d[2]:
        print("Yes")
    else:
        print("No")

