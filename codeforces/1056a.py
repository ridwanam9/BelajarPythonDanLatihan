n = int(input())
stops = {}
for _ in range(n):

    arr = list(map(int, input().split()))
    r = arr[0]
    arr.pop(0)

    for x in arr:
        if x not in stops:
            stops[x] = 1
        else:
            stops[x] += 1

# output = []
for x in stops.keys():
    if stops[x] == n:
        print(x, end=" ")
        # output.append(x)
# print(" ".join(sorted(output)))










# stops = {}

# arr = list(map(int, input().split()))
# r = arr[0]
# arr.pop(0)

# for x in arr:
#     if x not in stops:
#         stops[x] = 1
#     else:
#         stops[x] += 1

# print(stops)
# for x in stops.keys():
#     if stops[x] == 2:
#         print(x, end=" ")


