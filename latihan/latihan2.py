# Latihan 1 : Daftar Film
class Kontak:
    def __init__(self, nama, nomor_hp):
        self.nama = nama
        self.nomor_hp = nomor_hp
    
    def __str__(self):
        return f"{self.nama} oleh {self.nomor_hp}"
    
class Buku_Telepon:

    def __init__(self):
        self.daftar_kontak = []

    def tambah_kontak(self, kontak):
        self.daftar_kontak.append(kontak)
        
    def tampilkan_kontak(self):
        for x in self.daftar_kontak:
            print(x)

    def hapus_kontak(self, nama_kontak):
        for kontak in self.daftar_kontak:
            if kontak.nama.lower() == nama_kontak.lower():
                self.daftar_kontak.remove(kontak)
                print(f"Kontak {nama_kontak} berhasil dihapus.")
                return
        print(f"Kontak {nama_kontak} tidak ditemukan.")


        
kontak1 = Kontak("Ridwan", "0888888")
kontak2 = Kontak("Yusuf", "0888999")
buku_telepon = Buku_Telepon()
buku_telepon.tambah_kontak(kontak1)
buku_telepon.tambah_kontak(kontak2)
buku_telepon.tampilkan_kontak()
buku_telepon.hapus_kontak("Ridwan")
print("-"*10)
buku_telepon.tampilkan_kontak()

