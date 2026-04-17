def digit_sum(n):
    return sum(map(int, str(n)))

i = int(input())
for _ in range(i):
    x = int(input())
    count = 0
    
    for d in range(1, 82):
        y = x + d
        if digit_sum(y) == d:
            count += 1
    
    print(count)