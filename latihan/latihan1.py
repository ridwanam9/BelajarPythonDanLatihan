# Latihan 1 : Daftar Film
class Film:
    def __init__(self, judul, sutradara):
        self.judul = judul
        self.sutradara = sutradara
    
    def __str__(self):
        return f"{self.judul} oleh {self.sutradara}"
    
class Bioskop:

    def __init__(self):
        self.daftar_film = []

    def tambah_film(self, film):
        self.daftar_film.append(film)
        
    def tampilkan_film(self):
        for x in self.daftar_film:
            print(x)

    def cari_film(self, cari):
        ditemukan = False
        for film in self.daftar_film:
            if cari.lower() in film.judul.lower(): 
                print(f"Film ditemukan: {film}")
                ditemukan = True
        if not ditemukan:
            print("Film tidak ditemukan.")


film1 = Film("Interstellar", "Christopher Nolan")
film2 = Film("After Earth", "John")
bioskop = Bioskop()
bioskop.tambah_film(film1)
bioskop.tambah_film(film2)

bioskop.tampilkan_film()
# Output:
# Interstellar oleh Christopher Nolan
# After Earth oleh John

bioskop.cari_film("Interstellar")
bioskop.cari_film("After Earth")
# Output:
# Film ditemukan: Interstellar oleh Christopher Nolan
# Film ditemukan: After Earth oleh John