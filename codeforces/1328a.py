t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a < b:
        print(b-a)
    elif a >= b:
        if a%b == 0:
            print(0)
        else:
            print(((b*(a//b))+b)-a)
    

# contoh:
# a = 20
# b = 6

# 20 // 6 = 3
# 3 * 6 = 18
# 18 + 6 = 24
# 24 - 20 = 4

# ((b*(a//b))+b) - a
# ((6*(20//6))+6) - 20
# = 4