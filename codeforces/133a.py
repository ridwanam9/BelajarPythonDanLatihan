p = input()
s = [ord(x) for x in "HQ9+"]
is_Yes = False
for x in p:
    if ord(x) in s:
        is_Yes = True
        break
print("Yes" if is_Yes else "No")
# if is_Yes:
#     print("Yes")
# else:
#     print("Yes")
