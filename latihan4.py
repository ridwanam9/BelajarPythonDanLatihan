# Latihan 4: Class dan Method Sendiri

class Mobil:
    def __init__(self, nama_mobil):
        self.nama_mobil = nama_mobil

    def tampilkan_nama(self):
        print("Ini mobil" ,self.nama_mobil)

# Setelah class dibuat, berikut cara penggunaannya:
avanza = Mobil("Avanza")
avanza.tampilkan_nama()

# Output:
# Ini mobil Avanza
