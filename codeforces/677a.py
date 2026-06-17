n, h = map(int, input().split())
arr = list(map(int, input().split()))
width = 0
for x in arr:
    if x > h:
        width += 2
    else:
        width += 1
print(width)

