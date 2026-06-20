s = input()
hello = "hello"
i_hello = 0
for x in s:
    if i_hello == 5:
        break
    else:
        if x == hello[i_hello]:
            i_hello += 1
        
print("YES" if i_hello == 5 else "NO")