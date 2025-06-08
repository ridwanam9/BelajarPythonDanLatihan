
class Penulis:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []

    def tampilkan_buku(self):
        for x in self.daftar_buku:
            print (x)

class Buku(Penulis):

    def __init__(self, judul, tahun):
        self.judul = judul
        self.tahun = tahun
        self.penulis = Penulis.nama
    
    def tambah_buku(self):
        self.daftar_buku.append()
        
ari = Penulis("Ari")
buku_ari = Buku()


ari.tampilkan_buku()