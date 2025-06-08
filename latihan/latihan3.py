
class Tugas:
    def __init__(self, judul, deskripsi):
        self.judul = judul
        self.deskripsi = deskripsi
        self.selesai = False

    def __str__(self):
        status = "Selesai" if self.selesai else "Belum selesai"
        return f"{self.judul} - {self.deskripsi} ({status})"

class DaftarTugas:
    def __init__(self):
        self.list_tugas = []

    def tambah_tugas(self, tugas):
        self.list_tugas.append(tugas)

    def tampilkan_tugas(self):
        for tugas in self.list_tugas:
            print(tugas)

    def tandai_selesai(self, judul_tugas):
        for tugas in self.list_tugas:
            if tugas.judul.lower() == judul_tugas.lower():
                tugas.selesai = True
                print(f"Tugas '{judul_tugas}' ditandai selesai.")
                return
        print("Tugas tidak ditemukan.")



tugas1 = Tugas("Penambahan", "Menambahkan Angka")
Daftar_Tugas = DaftarTugas()
Daftar_Tugas.tambah_tugas(tugas1)
Daftar_Tugas.tampilkan_tugas()

