class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """

        reversed_prefix = word[word.index("d")::-1] + word[word.index("d")+1::]
        return reversed_prefix

print(Solution().reversePrefix("abcdefd", "d"))

