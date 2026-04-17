
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    
    if x >= 2*y and (x - 2*y) % 3 == 0:
        print("YES")
    else:
        print("NO")