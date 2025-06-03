# Latihan 6: Class dengan Validasi dan Pengubahan Nama
class Mahasiswa:
    jurusan_tersedia = ["Informatika", "Teknik Elektro", "Sistem Informasi", "Teknik Mesin"]

    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan

    def perkenalan(self):
        print(f"Halo, nama saya {self.nama} dari jurusan {self.jurusan}")

    def ubah_nama(self, nama_baru):
        self.nama = nama_baru

    def ganti_jurusan(self, jurusan_baru):
        if jurusan_baru in Mahasiswa.jurusan_tersedia:
            self.jurusan = jurusan_baru
        else:
            print(f"Jurusan {jurusan_baru} tidak tersedia.")

    def lihat_jurusan(self):
        print(f"Saya sekarang di jurusan {self.jurusan}")

   

budi = Mahasiswa("Budi", "Informatika")
budi.perkenalan()

budi.ubah_nama("Budi Hartono")
budi.perkenalan()

budi.ganti_jurusan("Teknik Mesin")   
budi.lihat_jurusan()

budi.ganti_jurusan("Kedokteran")    
