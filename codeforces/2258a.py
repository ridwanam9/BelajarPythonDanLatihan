# from math import gcd

# t = int(input())

# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))

#     g = gcd(a[0], a[-1])
#     divisors = []
#     d = 1

#     while d * d <= g:
#         if g % d == 0:
#             divisors.append(d)
#             if d != g // d:
#                 divisors.append(g // d)
#         d += 1
#     divisors.sort(reverse=True)

#     for x in divisors:
#         good = True
#         bad = 0
#         for i in range(n):
#             if a[i] % x != 0:
#                 bad += 1

#         good_count = n - bad
#         if good_count >= 2:
#             print(x)
#             break

def greatest_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    print(greatest_divisor(arr[0], arr[n - 1]))


