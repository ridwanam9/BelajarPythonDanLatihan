number1 = input()
number2 = input()
number3 = []
for i in range(len(number1)):
    if number1[i] != number2[i]:
        number3.append("1")
    else:
        number3.append("0")
print("".join(number3))
