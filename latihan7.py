# Latihan 7: Class Kelas Menampung Banyak Mahasiswa
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

class Kelas:
    def __init__(self, nama_kelas):
        self.nama_kelas = nama_kelas
        self.daftar_mahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.daftar_mahasiswa.append(mahasiswa)  # Tambah objek Mahasiswa ke list

    def tampilkan_semua(self):
        print(f"Mahasiswa dalam Kelas {self.nama_kelas}:")
        for mhs in self.daftar_mahasiswa:
            mhs.perkenalan()
        
   
m1 = Mahasiswa("Budi", "Informatika")
m2 = Mahasiswa("Ani", "Sistem Informasi")

kelas_a = Kelas("Kelas A")
kelas_a.tambah_mahasiswa(m1)
kelas_a.tambah_mahasiswa(m2)

kelas_a.tampilkan_semua()
