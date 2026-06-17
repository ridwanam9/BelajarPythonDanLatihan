n = int(input())
passengers = 0
max_number = 0
for _ in range(n):
    a, b = map(int, input().split())
    passengers += b - a
    if passengers > max_number:
        max_number = passengers

print(max_number)