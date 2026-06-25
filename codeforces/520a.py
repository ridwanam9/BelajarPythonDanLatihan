n = int(input())
s = input().lower()
x = [ord(x) for x in s]
is_there = True
for j in range(97, 123):
    if j in x:
        continue
    else:
        is_there = False
        break
print("YES" if is_there else "NO")



# print(ord("a"))
# print(ord("z"))