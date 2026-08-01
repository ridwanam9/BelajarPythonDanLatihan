# s, n = map(int, input().split())
# defeat_all_dragons = True
# for _ in range(n):
#     # print(f"kekuatan kirito: {s}")
#     x, y = map(int, input().split())
#     if s > x:
#         s += y
#     else:
#         defeat_all_dragons = False
#         break

# print("YES" if defeat_all_dragons else "NO")


s, n = map(int, input().split())
defeat_all_dragons = True
dragon_strenght_plus_increase = []

for _ in range(n):
    # print(f"kekuatan kirito: {s}")
    x, y = map(int, input().split())
    dragon_strenght_plus_increase.append([x,y])

sortir = sorted(dragon_strenght_plus_increase)
# for x,y in dragon_strenght_plus_increase:
#     if s > x:
#         s += y
#     else:
#         defeat_all_dragons = False
#         break

# print("YES" if defeat_all_dragons else "NO")

print(dragon_strenght_plus_increase)
print(sortir)