# n = int(input())
# x = list(map(int, input().split()))
# for i in x:
#     j = 0
#     for y in range(1, (i//2)+1):
#         if j > 2:
#             break
#         elif i%y == 0:
#             j += 1
#     print("YES" if j == 2 else "NO")



def is_Tprime(n):
    j = 0
    for y in range(1, (n//2)+1):
        if j > 2:
            break
        if n%y == 0:
            j += 1
    return "YES" if j == 2 else "NO"

print(is_Tprime(9))
print(is_Tprime(10))
print(is_Tprime(4))
print(is_Tprime(25))
print(is_Tprime(24))