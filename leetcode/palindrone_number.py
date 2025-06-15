class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        str_num = str(x)
        return str_num == str_num[::-1]

soal = Solution()
print(soal.isPalindrome(234))
print(soal.isPalindrome(232))
print(soal.isPalindrome(237))