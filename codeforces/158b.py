n = int(input())
s = list(map(int, input().split()))
if sum(s)%4 == 0:
    print(sum(s)//4)
else:
    print((sum(s)//4) + 1)