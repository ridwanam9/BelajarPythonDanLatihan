
def power(base, exponent):

    initial = base
    for x in range(exponent - 1):
        initial *= base
        # print(initial)
        x += 1

    return initial

print(power(2, 3))
print(power(2, 4))
print(power(3, 4))
print(power(3, 3))

