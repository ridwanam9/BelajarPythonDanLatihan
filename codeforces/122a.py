n = input()
if all(ch in "47" for ch in n):
    print("YES")
else:
    is_dividable = False
    for i in range(4, int(n)+1):
        if all(x in "47" for x in str(i)):
            if int(n)%i != 0:
                continue
            else:
                is_dividable = True
                break
    print("YES" if is_dividable else "NO")

