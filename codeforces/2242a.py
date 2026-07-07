t = int(input())
for _ in range(t):
    k = int(input())
    c = list(map(int, input().split()))

    memenuhi_syarat = False
    for x in c:
        if x > 2 or c.count(2) >= 2:
            memenuhi_syarat = True
            break
    print("YES" if memenuhi_syarat else "NO")




