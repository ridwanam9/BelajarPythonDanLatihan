def lengthOfLongestSubstring(s):
    if len(s) == 1:
        return 1

    subs = [] # untuk menampung char sementara
    len_numbers = 0
    count = 0

    for i in range(len(s)):
        # if i == 0:
        #     count += 1
        #     subs.append(s[i])

        if s[i] not in subs:
            count += 1
            subs.append(s[i])

        else:
            subs.clear()
            if count > len_numbers:
                len_numbers = count
            subs.append(s[i])
            count = 1
    
        if count > len_numbers:
            len_numbers = count


    return len_numbers
    
print(lengthOfLongestSubstring("au"))
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("dvdf")) #3