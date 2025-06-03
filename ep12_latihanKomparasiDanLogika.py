# +++++0----5++++8----11++++++

print( "+++++0----5++++8----11++++++")

inputUser = int(input("masukan angka nya\n:"))
print("angka = ", inputUser)

isKurangDari0 = inputUser < 0
print("Kurang dari 0: ", isKurangDari0)

isLebihDari5KurangDari8 = 5 < inputUser < 8
print("Lebih dari 5 dan Kurang dari 8: ", isLebihDari5KurangDari8)

isLebihDari1 = inputUser > 11
print("Lebih dari 11: ", isLebihDari1)

isCorrect = isKurangDari0 or isLebihDari5KurangDari8 or isLebihDari1
print("Maka nilai", inputUser, "bernilai", isCorrect)