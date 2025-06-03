# Kelas Terbuka - belajar python episode 7 input dari user

import time
start_time = time.time()



a = 2
b = 3
c = a + b
d = "Hai"
e = "Ridwan"
f = a * b
print("hello world")

# ini contoh print tipe data
print(type(a)) #output: int
print("ini adalah data: ", b , ", dengan tipe data: " , type(b))

print("----------")
# Ini adalah contoh casting/mengubah tipe data
g = float(a)
print(g)
print("Data g: ",g , " dengan tipe data: ", type(g))
print("----------")

# Ini adalah contoh input dari user
nama = input("Masukkan nama anda :")

# Contoh input data integer
data_umur = int(input("Masukkan umur :"))

# Contoh input data float
ipk = float(input("Masukkan nilai IPK :"))


print("Nama: ", nama, " , umur: ", data_umur, " , IPK: ", ipk)

# Contoh input data boolean
boolean = bool(int(input("Masukkan boolean :")))
print("Nilai Boolean: ", boolean)

print(time.time() - start_time, "detik")