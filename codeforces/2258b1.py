t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = sorted(list(map(int, input().split())))

    max_element = max(arr)

    brr = arr

    # x = pivot length to be cut
    max_number = 0
    x = 1

    while x <= max_element//2+1:

        for i in brr:
            if brr[i] > x:
                brr.append(brr[i]-x)
                brr[i] = x
        c = brr.count(x)
        if c > max_number:
            max_number = c
        brr.clear()
        brr = arr

    print(max_number)




