t = int(input())
for _ in range(t):
    n = int(input())
    is_prime = True
    for i in range(2, int((n+1)**0.5) + 1):
        if (n+1) % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Yes")
    else:
        print("No")
