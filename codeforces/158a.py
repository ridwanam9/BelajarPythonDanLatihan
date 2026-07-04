n, k = map(int, input().split())
a = list(map(int, input().split()))

if a[0] == 0:
    print(0)
elif a[k-1] != 0:
    count = 0   
    for x in a:
        if x >= a[k-1]:
            count += 1
    print(count)
elif a[k-1] == 0:
    count = 0   
    for x in a:
        if x > a[k-1]:
            count += 1
    print(count)



# Not Finished