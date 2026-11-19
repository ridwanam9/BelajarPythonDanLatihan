t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    withdraw_days = (n - k) + 1
    print(2**withdraw_days + (2*(k-1)))
