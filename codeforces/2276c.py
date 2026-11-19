t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    # example = n: 8, k: 2
    count = 0
    panjang_subarray = k + 1
    start_sub = 0
    end_sub = panjang_subarray
    while panjang_subarray <= n:
        # if sum(arr[start_sub:panjang_subarray]) % k == 0:
        #     start_sub += 1
        #     panjang_subarray += 1

        print(arr[start_sub:end_sub])
        start_sub += 1
        end_sub += 1

        if end_sub == n:
            start_sub = 0
            panjang_subarray += 1


