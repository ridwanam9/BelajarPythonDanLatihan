# Class Buku
#  Tahap 1: Struktur Dasar Program
class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def tampilkan_info(self):
        print(f"'{self.judul}' oleh {self.penulis} ({self.tahun})")


# Class Perpustakaan
class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)
        print(f"Buku '{buku.judul}' berhasil ditambahkan!")

    def tampilkan_semua_buku(self):
        if not self.daftar_buku:
            print("Belum ada buku dalam perpustakaan.")
        else:
            print("Daftar Buku:")
            for buku in self.daftar_buku:
                buku.tampilkan_info()


buku1 = Buku("Malice", "Ezekiel", "2024")
buku2 = Buku("Obelisk", "John", "2025")

Perpus1 = Perpustakaan()
Perpus1.tambah_buku(buku1)
Perpus1.tambah_buku(buku2)

Perpus1.tampilkan_semua_buku()