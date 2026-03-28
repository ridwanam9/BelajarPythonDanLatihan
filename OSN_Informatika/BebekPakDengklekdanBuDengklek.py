# n = int(input())
# arr = []

# for i in range(n):
#     x = int(input())
#     arr.append(x)

# for j in range(n-1,-1,-1):
#     print(arr[j])
    

import sys

n = int(sys.stdin.readline())
arr = [sys.stdin.readline().strip() for _ in range(n)]

sys.stdout.write("\n".join(arr[::-1]))