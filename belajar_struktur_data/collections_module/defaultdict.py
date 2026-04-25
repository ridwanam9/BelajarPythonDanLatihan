from collections import defaultdict
    

# Defining the dict
d = defaultdict(int)
    
L = [1, 2, 3, 4, 2, 4, 1, 2]
    
# Iterate through the list
# for keeping the count
# menghitung frekuensi
for i in L:
        
    # The default value is 0
    # so there is no need to
    # enter the key first
    d[i] += 1
        
print(d)
print(" ")
print(dict(d))



# Mengelompokan data
siswa = [("IPA", "Budi"), ("IPS", "Ani"), ("IPA", "Citra"), ("IPS", "Doni")]
kelas = defaultdict(list)

for jurusan, nama in siswa:
    kelas[jurusan].append(nama)

print(dict(kelas))
# {'IPA': ['Budi', 'Citra'], 'IPS': ['Ani', 'Doni']}


# Menyimpan nilai unik
tags = defaultdict(set)
tags["python"].add("programming")
tags["python"].add("programming")  # duplikat diabaikan
tags["python"].add("data science")

print(dict(tags))
# {'python': {'programming', 'data science'}}



# default factory custom
d = defaultdict(lambda: "tidak diketahui")
d["nama"] = "Budi"

print(d["nama"])    # Budi
print(d["umur"])    # tidak diketahui