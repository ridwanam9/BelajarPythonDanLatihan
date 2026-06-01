n = int(input())
a = list(map(int, input().split()))

def fpb(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def kpk(a, b):
    return abs(a * b) // fpb(a, b)

count = 0
for x in range(n):
    for j in range(x+1, n):
        if kpk(a[x], a[j]) < a[x] ^ a[j]:
            count += 1

print(count)
# print(pairs)


# pairs = []
#         pairs.append([a[x],a[j]])
        # if [a[x],a[j]] not in pairs:








