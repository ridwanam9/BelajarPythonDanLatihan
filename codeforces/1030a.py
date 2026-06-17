n = int(input())
arr = list(map(int, input().split()))
is_easy = True
for x in arr:
    if x == 1:
        is_easy = False
        break

print("EASY" if is_easy else "HARD")