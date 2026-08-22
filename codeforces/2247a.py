t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1 or n%2 != 0:
        print("no")
    elif sum(a) == 0:
        print("yes")
    else:
        is_true = False
        for i in range(n-1):
            a[i] = a[i]*-1
            a[i+1] = a[i+1]*-1
            if sum(a) == 0:
                is_true = True
                break
            else:
                a[i] = a[i]*-1
                a[i+1] = a[i+1]*-1

        print("yes" if is_true else "no")


