n = int(input())
a = list(map(int, input().split()))
eveness = []
for x in a:
    if x%2 == 0:
        eveness.append("even")
    else:
        eveness.append("odd")
if eveness.count("even") > eveness.count("odd"):
    print(eveness.index("odd")+1)
else:
    print(eveness.index("even")+1)
