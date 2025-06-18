# Kalimat Terbalik
# Buat fungsi reverse_sentence(sentence) yang membalik urutan kata dalam kalimat (bukan membalik huruf).


def reverse_sentence(sentence):

    words = sentence.split()
    words.reverse()

    reverse_list = " ".join(words)
    print(reverse_list)


reverse_sentence("saya belajar python")
# Output: "python belajar saya"