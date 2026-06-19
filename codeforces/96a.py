st = input()
count = 1
for i in range(len(st)-1):
    if count == 7:
        break
    elif st[i] == st[i+1]:
        count += 1
    else:
        count = 1
print("YES" if count >= 7 else "NO")