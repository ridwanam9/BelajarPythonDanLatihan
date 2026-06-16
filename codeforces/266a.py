n = int(input())
stones = input()
count = 0
if len(stones) == 1:
    print(0)
else:
    for x in range(n-1):
        if stones[x] == stones[x+1]:
            count += 1
    print(count)
