# s = input().lower()
# print(chr(ord(s[0])-32)+s[1:])


s = input()
arr = list(s)
uppers = [chr(x) for x in range(65, 91)]
lowers = [chr(x) for x in range(97, 123)]
if arr[0] in uppers and arr[1::] in lowers:
    print(s)
elif arr[0] in uppers and arr[1::] in uppers:
    print(s.lower())
# elif arr[0] in lowers and arr[1::] in uppers:










# lowers = [chr(x) for x in range(97,123)]
# print(chr(65))
# print(f"A = {ord("A")}") #65
# print(f"Z = {ord("Z")}") #90
# print(f"a = {ord("a")}") #97
# print(f"z = {ord("z")}") #122


# for i in range(65, 123):
#     print(f"{i} = {chr(i)}")