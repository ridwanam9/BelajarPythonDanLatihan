t = int(input())
for _ in range(t):
    n, c = input().split()
    n = int(n)
    s = input()

    count = 0
    if s == s[::-1]:
        print(0)
    else:
        if n%2 == 0:
            a = s[:n//2:]
            b = s[:(n//2)-1:-1]
            for i in range(n//2):
                if a[i] != b[i]:
                    if a[i] != c and b[i] != c:
                        count += 2
                    elif a[i] == c or b[i] == c:
                        count += 1

        else:
            a = s[:n//2:]
            b = s[:(n//2):-1]
            for i in range(n//2):
                if a[i] != b[i]:
                    if a[i] != c and b[i] != c:
                        count += 2
                    elif a[i] == c or b[i] == c:
                        count += 1
        print(count)
 


























