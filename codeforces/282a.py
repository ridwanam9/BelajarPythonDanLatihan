n = int(input())
x = 0
for _ in range(n):
    st = input()
    if st == "X++":
        x +=1
    if st == "++X":
        x +=1
    if st == "X--":
        x -=1
    if st == "--X":
        x -=1

print(x)