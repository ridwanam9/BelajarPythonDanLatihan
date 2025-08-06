class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        
        for row in image:
        # Flip: reverse row
            row.reverse()
            # Invert: change 0 to 1 and 1 to 0
            for i in range(len(row)):
                row[i] = 1 - row[i]
        return image


print(Solution().flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))