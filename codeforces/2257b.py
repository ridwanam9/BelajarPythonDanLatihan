t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))

    count_arr = arr[-1]
    count_brr = brr[-1]
    if len(arr) > 1:
        for i in range(n-1):
            count_arr += (arr[i]-arr[i+1]) + 1
    if len(brr) > 1:
        for i in range(m-1):
            count_brr += (brr[i]-brr[i+1]) + 1

    if count_brr > count_arr:
        print(2)
    else:
        print(1)
