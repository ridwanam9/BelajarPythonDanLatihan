t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    srr = []
    abrev_arr = []
    for _ in range(n):
        s = input()
        srr.append(s[0].upper())
    for _ in range(m):
        ab = input()
        abrev_arr.append(ab)
    # print(srr)
    # print(abrebv_arr)
    set_abrev = "".join(abrev_arr)
    is_there = True
    for x in set_abrev:
        if x not in srr:
            is_there = False
    print("Yes" if is_there else "No")




    
        

