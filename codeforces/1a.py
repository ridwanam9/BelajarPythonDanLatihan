n, m, a = map(int, input().split())
x = 1
y = 1
if n > a and m > a:
    if n%a == 0:
        x = n//a
    else:
        x = (n//a)+1
    if m%a == 0:
        y = m//a
    else:
        y = (m//a)+1
elif n <= a and m > a:
    if m%a == 0:
        y = m//a
    else:
        y = (m//a)+1
elif n > a and m <= a:
    if n%a == 0:
        y = n//a
    else:
        y = (n//a)+1
else:
    x = 1
    y = 1
print(x*y)