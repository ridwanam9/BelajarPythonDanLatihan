class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        count = 0
        for x in words:
            if x == x[::-1]:
                count += 1
                break
        if count == 0:
            return ""
        return x
            

print(Solution().firstPalindrome(["abc","car","ada","racecar","cool"]))
print(Solution().firstPalindrome(["abc","car","cool"]))
print(Solution().firstPalindrome(["level","car","cool"]))
print(Solution().firstPalindrome(["abc","car","cool", "lalalal"]))