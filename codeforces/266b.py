n, t = map(int, input().split())
s = list(input())
iteration = 1
boys_position = []
while iteration <= t:
    for i in range(n-1):
        if s[i] == "B":
            boys_position.append(i)
    for j in boys_position:
        if s[j+1] == "G":
            s[j] = "G"
            s[j+1] = "B"
        else:
            continue

    iteration += 1

print("".join(s))


# contoh:
# 6 3
# input:
# BGGBBG

# output:
# 0
# GBGBGB
# 1
# GGBGBB
# 2
# GGGBBB