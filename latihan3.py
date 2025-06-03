#  Latihan 3: Dictionary Methods

# Diberikan dictionary berikut:
mahasiswa = {
    "nama": "Budi",
    "umur": 21,
    "jurusan": "Informatika"
}

# TODO: Cetak semua key
for x in mahasiswa.keys():
  print(x)


print("-"*10)

# TODO: Cetak semua value
for y in mahasiswa.values():
  print(y)


print("-"*10)


# TODO: Cetak nilai dari key "jurusan"
z = mahasiswa["jurusan"]
print(z)