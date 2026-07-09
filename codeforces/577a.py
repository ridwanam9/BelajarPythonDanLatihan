n, k = map(int, input().split())
if k > n**2:
    print(0)
else:
    count = 0
    for i in range(1, n+1):
        if k%i == 0 and k//i <= n:
            count += 1
    print(count)
