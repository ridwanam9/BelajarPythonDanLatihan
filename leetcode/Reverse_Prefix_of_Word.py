class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        
        ch_index = word.find(ch)
        reversed_prefix = word[ch_index::-1] + word[ch_index+1::]
        if not ch in word:
            return word
        return reversed_prefix

print(Solution().reversePrefix("abcdefd", "d"))

