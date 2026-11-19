# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     for i in arr:
#         if i <= 1:
#             print(i)
#         else:
#             night = 2
#             # print(f"night: {1}")
#             # print(i)
#             numbers = [i]
#             while i > 1:
#                 y = 0
#                 # print(f"night: {night}")
#                 for x in str(i):
#                     y += int(x)*int(x)
#                 i = y
#                 # print(i)
#                 night += 1
#                 if y in numbers:
#                     break
#                 else:
#                     numbers.append(y)
#                     # print(numbers)
#             print(i)
#             # print(i)




arr = list(map(int, input().split()))
for i in arr:
    if i <= 1:
        print(i)
    else:

        # print(f"night: {1}")
        # print(i)
        numbers = [i]
        while i > 1:
            y = 0
            # print(f"night: {night}")
            for x in str(i):
                y += int(x)*int(x)
            i = y
            # print(i)

            if y in numbers:
                break
            else:
                numbers.append(y)
                # print(numbers)
        print(i)
        # print(i)