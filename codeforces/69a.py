n = int(input())
vx = 0
vy = 0
vz = 0
for _ in range(n):
    x, y ,z = map(int, input().split())
    vx += x
    vy += y
    vz += z

if vx == 0 and vy == 0 and vz == 0:
    print("YES")
else:
    print("NO")
