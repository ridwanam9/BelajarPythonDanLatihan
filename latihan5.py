# Latihan 5: Class dengan Beberapa Method
class Mahasiswa:
    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan

    def perkenalan(self):
        print(f"Halo, nama saya {self.nama} dari jurusan {self.jurusan}")

    def ganti_jurusan(self, jurusan_baru):
        self.jurusan = jurusan_baru

    def lihat_jurusan(self):
        print(f"Saya sekarang di jurusan {self.jurusan}")   


budi = Mahasiswa("Budi", "Informatika")
budi.perkenalan()

budi.ganti_jurusan("Teknik Elektro")
budi.lihat_jurusan()
