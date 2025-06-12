# 7. Palindrome Checker
def is_palindrome(s):
    # your code here
    
    # if s[::] == s[::-1]:
    if s.lower()[::] == s.lower()[::-1]:
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")


is_palindrome("level")
is_palindrome("Level")
is_palindrome("makananan")

print("\n")
# 8. Fibonacci ke-n
def fibonacci(n):
    
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)

print("\n")
# 9. Cek Anagram
def is_anagram(s1, s2):
    
    list1 = []
    for x in s1:
        # x.lower()
        list1.append(x)
        list1.sort()
    # print(list1)

    list2 = []
    for y in s2:
        # y.lower()
        list2.append(y)
        list2.sort()
    # print(list2)

    if list1 == list2:
        print("are anagrams")
    else:
        print("not anagrams")


is_anagram("aku", "saya")
is_anagram("aku", "kua")
is_anagram("asing", "singa")
is_anagram("aku", "aKu")