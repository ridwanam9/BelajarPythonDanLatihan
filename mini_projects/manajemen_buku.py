# Class Buku
import json


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

        # Menyimpan data ke file
    def simpan_ke_file(self, nama_file):
        data = [
            {"judul": b.judul, "penulis": b.penulis, "tahun": b.tahun}
            for b in self.daftar_buku
        ]
        with open(nama_file, "w") as f:
            json.dump(data, f)
        print(f"Data disimpan ke '{nama_file}'.")

    def muat_dari_file(self, nama_file):
        try:
            with open(nama_file, "r") as f:
                data = json.load(f)
                self.daftar_buku = [Buku(**item) for item in data]
            print(f"Data berhasil dimuat dari '{nama_file}'.")
        except FileNotFoundError:
            print(f"File '{nama_file}' tidak ditemukan.")

        
def menu():
    perpus = Perpustakaan()
    nama_file = "buku.json"

    while True:
        print("\n=== Menu Perpustakaan ===")
        print("1. Tambah Buku")
        print("2. Lihat Semua Buku")
        print("3. Cari Buku")
        print("4. Edit Buku")
        print("5. Hapus Buku")
        print("6. Simpan ke File")
        print("7. Muat dari File")
        print("0. Keluar")

        while True:
            pilihan = input("Pilih menu (0-7): ")
            if pilihan in [str(i) for i in range(8)]:
                break
            print("Masukkan angka antara 0 sampai 7.")


        if pilihan == "1":
            judul = input("Judul: ")
            penulis = input("Penulis: ")
            while True:
                tahun = input("Tahun Terbit: ")
                if tahun.isdigit():
                    tahun = int(tahun)
                    break
                else:
                    print("Masukkan tahun berupa angka.")
            buku = Buku(judul, penulis, int(tahun))
            perpus.tambah_buku(buku)

        elif pilihan == "2":
            perpus.tampilkan_semua()

        elif pilihan == "3":
            keyword = input("Kata kunci judul: ")
            perpus.cari_buku(keyword)

        elif pilihan == "4":
            judul = input("Judul buku yang ingin diedit: ")
            tahun_baru = input("Tahun terbit baru: ")
            perpus.edit_buku(judul, int(tahun_baru))

        elif pilihan == "5":
            judul = input("Judul buku yang ingin dihapus: ")
            perpus.hapus_buku(judul)

        elif pilihan == "6":
            perpus.simpan_ke_file(nama_file)

        elif pilihan == "7":
            perpus.muat_dari_file(nama_file)

        elif pilihan == "0":
            print("Terima kasih! Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    menu()


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

# Simpan ke file
perpus.simpan_ke_file("buku.json")

# Hapus semua data dari daftar
perpus.daftar_buku = []
print("\nSetelah penghapusan manual:")
perpus.tampilkan_semua()

# Muat ulang dari file
perpus.muat_dari_file("buku.json")
print("\nSetelah memuat ulang:")
perpus.tampilkan_semua()

print("-"*20)

