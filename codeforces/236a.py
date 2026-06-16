name = input()

chars = []
for x in name:
    if x in chars:
        continue
    else:
        chars.append(x)

if len(chars) % 2==1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")