# mencari semua bilangan prima dari 2 hingga n
def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return [i for i in range(2, n + 1) if is_prime[i]]


print(sieve_of_eratosthenes(50))



# Baris 1: def sieve_of_eratosthenes(n):

# Definisi fungsi yang menerima satu parameter n — batas atas pencarian bilangan prima. Fungsi ini akan mencari semua prima dalam rentang [2, n].

# Baris 2: is_prime = [True] * (n + 1)

# Ini bikin sebuah list boolean sepanjang n + 1 elemen, semuanya diisi True.

# Kenapa n + 1, bukan n? Karena kita mau index list-nya langsung mencerminkan angkanya. Index 0 mewakili angka 0, index 1 mewakili angka 1, ..., index n mewakili angka n. Kalau cuma n elemen, angka n sendiri gak akan punya tempat (index-nya out of range).
# Anggapan awal: semua angka dianggap prima (True) sampai terbukti sebaliknya. Ini prinsip dasar sieve — kita mulai optimis, lalu "mencoret" (set jadi False) yang ternyata komposit.

# Contoh kalau n = 10: is_prime = [True, True, True, True, True, True, True, True, True, True, True] (11 elemen, index 0-10).

# Baris 3: is_prime[0] = is_prime[1] = False

# 0 dan 1 bukan bilangan prima menurut definisi matematis (prima harus punya tepat dua faktor: 1 dan dirinya sendiri; 0 dan 1 gak memenuhi itu). Jadi kita langsung set keduanya False di awal, sebelum proses pencoretan dimulai.

# Ini penting — kalau dilewatkan, nanti fungsi akan salah menganggap 1 sebagai prima.

# Baris 5: for i in range(2, int(n**0.5) + 1):

# Ini loop utama yang mengontrol angka mana yang jadi "pencoret" berikutnya. Ada beberapa hal yang perlu dibedah di sini:

# n**0.5 — ini menghitung akar kuadrat dari n (misal kalau n=100, hasilnya 10.0). Kenapa cuma perlu sampai √n? Karena kalau ada angka komposit x ≤ n, pasti x punya faktor yang ≤ √x ≤ √n. Jadi semua komposit pasti sudah "ketangkap" oleh salah satu prima ≤ √n. Gak perlu cek lebih jauh dari itu.
# int(...) — membungkus hasil n**0.5 (yang berupa float) jadi integer, karena range() gak bisa nerima float. Ini otomatis membulatkan ke bawah (floor).
# + 1 — karena range() itu eksklusif di batas atas (gak termasuk angka terakhirnya), kita tambah 1 supaya angka int(n**0.5) itu sendiri ikut ter-cover di loop.
# Mulai dari 2 — karena 2 adalah bilangan prima terkecil, dan angka 0-1 sudah kita tangani terpisah.

# Contoh: kalau n = 50, maka n**0.5 ≈ 7.07, int(7.07) = 7, jadi loop-nya range(2, 8) → i akan bernilai 2, 3, 4, 5, 6, 7.

# Baris 6: if is_prime[i]:

# Ini pengecekan penting: kita cuma proses i sebagai pencoret kalau i sendiri masih berstatus prima (belum tercoret oleh iterasi sebelumnya).

# Kenapa perlu dicek? Karena loop di baris 5 berjalan untuk semua angka dari 2 sampai √n, termasuk angka komposit seperti 4, 6. Tapi kalau i = 4, misalnya, is_prime[4] sudah False (karena sudah dicoret waktu i = 2). Jadi gak perlu buang waktu mencoret kelipatan 4 lagi — itu semua sudah tercoret lewat kelipatan 2. Pengecekan ini yang bikin algoritma tetap efisien.

# Baris 7: for j in range(i * i, n + 1, i):

# Ini loop dalam yang mencoret semua kelipatan i. Tiga bagian range() di sini penting semua:

# Mulai dari i * i, bukan i * 2 — ini bagian paling sering ditanya. Alasannya: semua kelipatan i yang lebih kecil dari i * i (yaitu 2i, 3i, 4i, ..., (i-1)i) sudah pasti tercoret duluan oleh prima yang lebih kecil dari i. Contoh konkret: waktu i = 5, kelipatan 2×5=10, 3×5=15, 4×5=20 sudah tercoret waktu i=2 (untuk 10, 20) dan i=3 (untuk 15). Jadi mulai dari 5×5=25 aja sudah cukup — hemat banyak operasi.
# Batas atas n + 1 — supaya angka n sendiri (kalau kelipatan i) ikut tercoret, karena range() eksklusif.
# Step i — artinya lompat per i angka: i*i, i*i+i, i*i+2i, .... Ini cara efisien menghasilkan semua kelipatan i tanpa perlu pengecekan modulo (% i == 0) satu-satu.
# Baris 8: is_prime[j] = False

# Aksi "mencoret" yang sebenarnya — menandai index j (yang merupakan kelipatan dari i) sebagai bukan prima.

# Baris 10: return [i for i in range(2, n + 1) if is_prime[i]]

# Ini list comprehension yang mengumpulkan hasil akhir:

# range(2, n + 1) — iterasi semua angka dari 2 sampai n (mulai dari 2 karena 0 dan 1 sudah pasti bukan prima).
# if is_prime[i] — filter, cuma ambil angka yang statusnya masih True (belum pernah tercoret).
# Hasilnya list berisi semua bilangan prima dalam rentang [2, n].

# Catatan kecil: variabel i di sini bukan variabel i yang sama dengan di loop baris 5 — scope-nya beda, kebetulan namanya sama aja. Kalau mau lebih jelas bisa diganti jadi nama lain seperti x, tapi secara fungsional tidak masalah.

# is_prime = [True]*5
# print(is_prime)