
t = int(input())

for _ in range(t):
    x0, y0, r = map(int, input().split())
    x = x0 + r
    y = y0
    print(x, y)
