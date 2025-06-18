# Cek Pangram
# Buat fungsi is_pangram(text) yang mengecek apakah text mengandung seluruh huruf a-z minimal satu kali.


def is_pangram(words):
    letters = "abcdefghijklmnopqrstuvwxyz"

    lower = words.lower()

    text = lower.split()

    words_to_string = "".join(text)

    text = list(words_to_string)

    set_text = set(text)

    text = list(set_text)

    text = sorted(text)

    words_to_string = "".join(text)

    if words_to_string == letters:
        return True
    else:
        return False
    


print(is_pangram("the quick brown fox jumps over the lazy dog"))
print(is_pangram("abqrstuvwxyzmnopcdefghijkl"))
print(is_pangram("abqrstuvwx"))
# Output: True