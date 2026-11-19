t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())

    if (a+b+c) % 3 == 0 and max(a, b, c) - min(a, b, c) == 2:
        print("YES")
    else:
        print("NO")
        
