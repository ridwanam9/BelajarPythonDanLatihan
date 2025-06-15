# Buat fungsi top_words(text, k) yang mengembalikan k kata yang paling sering muncul dari text.

# Contoh:

# top_words("saya belajar python python saya suka python", 2)
# Hasil:

# [('python', 3), ('saya', 2)]

def top_words(text, k):

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

    sorted_words = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
        

    return sorted_words[:k]

print(top_words("saya belajar python python saya suka python", 2))