s = input()

if s == "{}":
    print(0)
else:
    arr = []
    for x in range(1, len(s)-1, 3):
        if s[x] in arr:
            continue
        else:
            arr.append(s[x])
    print(len(arr))






s = "1234567890"
print(s[::1])
print(s[::2])
print(s[::3])