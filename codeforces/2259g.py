# from bisect import bisect_right

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    b = [arr[i] - i * k for i in range(n)]

    prefix = [0] * n
    prefix[0] = arr[0]

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]

    ans = [0] * n

    for i in range(1, n - 1):
        target = arr[i - 1] - i * k

        lo = i + 1
        hi = n - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if b[mid] <= target:
                hi = mid - 1
            else:
                lo = mid + 1

        num = lo - i - 1

        ans[i] = (
            prefix[i + num]
            - prefix[i]
            - k * num * (num + 1) // 2
            - arr[i - 1] * num
        )
    print(*ans)






# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     arr = list(map(int, input().split()))

#     if k > arr[-1]:
#         crr = [0]*n
#         print(*crr) 
#     else:
#         crr = []
#         i = 0
#         while i <= n-1:
#             brr = [arr[x] for x in range(n) if x != i]
#             count = 0
#             for j in range(len(brr)-1):
#                 if brr[j+1] - brr[j] > k:
#                     count += brr[j+1] - (brr[j] + k) 
#                     brr.pop(j+1)
#                     brr.insert(j+1, brr[j]+k)
#             crr.append(count)
#             i += 1
#         print(*crr)
