n, k = map(int, input().split())
while k > 0:
    if n > 9 and n % 10 == 0: #jika digit terakhir nol
        n //= 10
        k -= 1
    elif n > 9 and n % 10 !=0: #jika digit terakhir bukan nol
        n -= 1
        k -= 1
    else:
        n -= 1
        k -= 1

print(n)