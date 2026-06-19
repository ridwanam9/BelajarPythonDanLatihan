# Menggunakan dictionary
n = int(input())
database = {}
for _ in range(n):
    name = input()
    if name not in database:
        database[name] = 1
        print("OK")
    else:
        database[name] += 1
        print(f"{name}{database[name]-1}")


