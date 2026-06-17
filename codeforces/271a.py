y = int(input()) + 1
chars = []
while len(chars) < 4:
    st_y = str(y) 
    for x in st_y:
        if x in chars:
            chars.clear()
            y += 1
            break
        else:
            chars.append(x)

print("".join(chars))

