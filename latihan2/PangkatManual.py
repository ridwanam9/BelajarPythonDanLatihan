
def power(base, exponent):

    # for x in range(exponent):
    #     print(x)

    # return base**exponent

    # i = 1
    # while 1 < exponent + 1:
    #     base *= base
    #     print(base)
    #     i += 1

    # return base

    initial = base
    for x in range(exponent - 1):
        initial *= base
        # print(initial)
        x += 1

    return initial

print(power(2, 3))
print(power(2, 4))
print(power(2, 6))
print(power(2, 2))
# Output: 8  (karena 2 * 2 * 2 = 8)
