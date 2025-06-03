# Kelas Terbuka - belajar python episode 10 komparasi


a = 6
b = 7
c = 7

print("Nilai a:",a)
print("Nilai b:",b)

print("")
# Ini adalah contoh komparasi <, >, <=, >=, ==, !=
h = a > b
print("Apakah a > b true atau false: ",h)
i = a < b
print("Apakah a < b true atau false: ",i)

print("")
# Ini adalah contoh penggunaan is sebagai pembanding dua variabel


# Ini adalah nilai hex identity untuk komparasi, jika nilai berbeda maka is bernilai false
print("Nilai hex a:", hex(id(a)))
print("Nilai hex b:", hex(id(b)))

print("")
# Contoh komparasi is dan is not
d = a is b
print("hasil a is b:", d)

e = a is not b
print("hasil a is not b:", e)

