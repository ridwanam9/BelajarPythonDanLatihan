t = int(input())
for _ in range(t):
    s = input()
    count_A = 0
    count_B = 0
    for i in range(3):

        count_A += int(s[i])

    for j in range(len(s)-3, len(s)):
        count_B += int(s[j])

    if count_A == count_B:
        print("Yes")
    else:
        print("No")

    







# n = "1234567890"
# print(n[:3:])
# print(n[-3::])


# print(sum(int(n[:3:])))
# print(sum(int(n[:3:])))