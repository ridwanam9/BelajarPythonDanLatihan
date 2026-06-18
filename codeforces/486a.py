n = int(input())
if n%2 == 1:
    print(-n + ((n-1)//2))
else:
    print(n//2)



# contoh:
# n = 8
# rumus: ((-1)**n)*n
# -1+2-3+4-5+6-7+8
# (-1+2)+(-3+4)+(-5+6)+(-7+8)
# 1+1+1+1 = 4
# berarti rumusnya:
# n//2

# n = 7
# rumus: ((-1)**n)*n
# -1+2-3+4-5+6-7
# (-1+2)+(-3+4)+(-5+6)-7
# 1+1+1-7 = -4
# berarti rumusnya:
# -n + ((n-1)//2) atau -((n+1)//2)

