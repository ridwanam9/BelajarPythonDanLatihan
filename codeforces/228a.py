s = list(map(int, input().split()))
distinct = []
for x in s:
    if x in distinct:
        continue
    else:
        distinct.append(x)

print(len(s)-len(distinct))