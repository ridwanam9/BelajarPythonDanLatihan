n = int(input())
p = list(map(int, input().split()))
j = []
for i in range(1, n+1):
    print(f"j[p[{i}-1]-1]")
    print(f"j[p[{i-1}]-1]")
    print(f"j[{p[i-1]}-1]")
    print(f"j[{p[i-1]-1}]")
    print(f"{i}")
    print("-------")
    j.insert(p[i-1]-1, i)
print(*j)






# p = []
# p.insert(1, "B")
# print(p)
# p.insert(0, "A")
# print(p)