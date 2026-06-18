n = int(input())
magnets = []
count = 1
for i in range(n):
    char = input()
    if i > 0:
        magnets.append(char)
        if magnets[i] != magnets[i-1]:
            count += 1
    else:
        magnets.append(char)

print(count)


