t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    for i in range(n):
        left = i + 1
        right = n - i
        ans = 2 * min(left, right) - 1
        print(ans, end=' ')
    print()


# print(2%3)
# print(f"{"2 "*3}")

# arr = [1,2,3,4,5,]
# print(arr)
# print(*arr)