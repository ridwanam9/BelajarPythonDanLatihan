n = int(input())
data1 = list(map(int, input().split()))
data2 = list(map(int, input().split()))

p = data1[0]
parr = data1[1:]
q = data2[0]
qarr = data2[1:]


if qarr[-1] >= n or parr[-1] >= n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")





# print(p)
# print(parr)
# print(q)
# print(qarr)