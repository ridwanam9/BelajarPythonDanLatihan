st = input().lower()

vowels = ["a","i","y","u","e","o"]
consonant = []
for x in st:
    if x in vowels:
        continue
    else:
        consonant.append(x)

for i in range(len(consonant)):
    consonant.insert(i, "."+consonant[i])
    consonant.remove(consonant[i+1])
print("".join(consonant))