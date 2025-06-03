# Kelas Terbuka - belajar python episode 6 casting tipe data

import time
start_time = time.time()



a = 2
b = 3
c = a + b
d = "Hai"
e = "Ridwan"
f = a * b
print("hello world")
print("Hello Ridwan")

print("World")
# ini contoh tipe data
print(type(a)) #output: int
print("ini adalah data: ", b , ", dengan tipe data: " , type(b))


print("----------")
# Ini adalah contoh casting tipe data
g = float(a)
print(g)
print("Data g: ",g , " dengan tipe data: ", type(g))
print("----------")

print(time.time() - start_time, "detik")