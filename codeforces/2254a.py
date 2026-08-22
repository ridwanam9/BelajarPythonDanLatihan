t = int(input())
for _ in range(t):
    arr = sorted(list(map(int, input().split())))

    round_n = 0
    store = []
    if round_n == 0:
        for x in arr:
            if x not in store:
                store.append(x)
    while len(store) == 3:
        arr[2] -= 1
        arr[0] += 1
        store.clear()
        for x in arr:
            if x not in store:
                store.append(x)
        round_n += 1

    print(round_n)


