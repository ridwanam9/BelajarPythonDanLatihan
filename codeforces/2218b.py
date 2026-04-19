# t = int(input())
# for _ in range(t):
#     arr = list(map(int, input().split()))

#     i = 0
#     l = 0
    
#     # mencari nilai terbesar
#     for x in range(7):
#         if arr[x] > l:
#             l = arr[x]
#             i = x

#     # menghitung hasil
#     for j in range(7):
#         if j != i:
#             l -= arr[j]

#     print(l)


t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    
    total = sum(arr)
    mx = max(arr)
    
    print(2*mx - total)