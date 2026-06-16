st = input()
lowers = 0
uppers = 0
for x in st:
    if ord(x) <= 90:
        uppers += 1
    else:
        lowers += 1
if lowers >= uppers:
    print(st.lower())
else:
    print(st.upper())
