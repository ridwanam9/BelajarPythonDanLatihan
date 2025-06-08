# Class Buku
class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def __str__(self):
        return f"'{self.judul}' oleh {self.penulis} ({self.tahun})"


# Class Perpustakaan
class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)
        print("Buku berhasil ditambahkan.")

    def tampilkan_semua(self):
        if not self.daftar_buku:
            print("Belum ada buku.")
        else:
            print("daftar Buku:")
            for buku in self.daftar_buku:
                print(buku)

    def cari_buku(self, keyword):
        hasil = [b for b in self.daftar_buku if keyword.lower() in b.judul.lower()]
        if hasil:
            for b in hasil:
                print(f"Ditemukan: {b}")
        else:
            print("Buku tidak ditemukan.")

    def edit_buku(self, judul, ganti_tahun):
        for buku in self.daftar_buku:
            if buku.judul.lower() == judul.lower():
                buku.tahun = ganti_tahun
                print(f"Buku '{judul}' diedit. tahun terbit = {ganti_tahun}")
                return
        print(f"Buku '{judul}' tidak ditemukan.")

    def hapus_buku(self, judul):
        for buku in self.daftar_buku:
            if buku.judul.lower() == judul.lower():
                self.daftar_buku.remove(buku)
                print(f"Buku '{judul}' dihapus.")
                return
        print(f"Buku '{judul}' tidak ditemukan.")


# Inisialisasi perpustakaan
perpus = Perpustakaan()

# Tambah beberapa buku
b1 = Buku("Laskar Pelangi", "Andrea Hirata", 2005)
b2 = Buku("Negeri 5 Menara", "Ahmad Fuadi", 2009)

perpus.tambah_buku(b1)
perpus.tambah_buku(b2)

# Tampilkan semua buku
perpus.tampilkan_semua()

# Cari buku
perpus.cari_buku("Laskar")

# Hapus buku
# perpus.update_buku("Laskar Pelangi", 2010)
perpus.edit_buku("Laskar Pelangi", 2010)

perpus.tampilkan_semua()

perpus.edit_buku("Negeri 5 Menara", 2015)

perpus.tampilkan_semua()
# perpus.hapus_buku("Laskar Pelangi")

