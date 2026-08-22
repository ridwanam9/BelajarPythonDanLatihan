t = int(input())
for _ in range(t):
    n = int(input())
    if_any = False
    for b in range(0,n+1,12):
        a = n-b
        str_a = str(a)
        if str_a == str_a[::-1]:
            if_any = True
            break
    if if_any:
        print(a,b)
    else:
        print(-1)






# # n +1
# n = 72
# for i in range(0,n+1,12):
#     print(i)


# s = "nama"
# print(s)
# print(s[::-1])