st = input()
numbers = [x for x in st if x != "+"]
print("+".join(sorted(numbers)))

