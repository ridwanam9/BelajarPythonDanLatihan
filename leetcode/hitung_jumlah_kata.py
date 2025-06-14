# Hitung Jumlah Kata (Manual Tanpa defaultdict)
# Deskripsi:
# Buat fungsi count_words(text) yang menerima string kalimat, dan menghitung berapa kali setiap kata muncul.

def count_words(text):
    words = text.lower().split()
    count_dict = {}

    for word in words:
        if word in count_dict:
            count_dict[word] += 1
            pass
        else:
            # masukkan word ke dict dengan nilai 1
            count_dict[word] = 1
            pass

    return count_dict



print(count_words("halo nama saya ridwan halo"))