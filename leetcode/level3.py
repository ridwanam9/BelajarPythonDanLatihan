# 7. Palindrome Checker
def is_palindrome(s):
    return s.lower() == s.lower()[::-1]

print(is_palindrome("Level"))  # True
print(is_palindrome("makananan"))  # False


print("\n")
# 8. Fibonacci ke-n
def fibonacci(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci(10))


print("\n")
# 9. Cek Anagram
def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

print(is_anagram("aku", "kua"))    # True
print(is_anagram("asing", "singa"))  # True
print(is_anagram("aku", "saya"))   # False
