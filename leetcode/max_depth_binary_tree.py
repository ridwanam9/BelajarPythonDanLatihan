# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:  # kalau kosong
            return 0
        # kedalaman = 1 + maksimum dari kedalaman kiri & kanan
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# Solution().maxDepth([3,9,20,null,null,15,7])

