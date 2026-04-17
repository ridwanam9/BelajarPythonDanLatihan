
def nums_digit(n):
    digits=0
    for x in range(1, n+1):
        digits += len(str(x))
    return digits

print(nums_digit(13))
print(nums_digit(4))








# n = 10
# m = str(n)
# print(len(str(n)))