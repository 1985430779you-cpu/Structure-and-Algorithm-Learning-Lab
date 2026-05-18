class TreeNode():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root):
        ans = float("-inf")
        def findLargestSum(node):
            if not node:
                return 0
            left = findLargestSum(node.left)
            right = findLargestSum(node.right)
            if left < 0:
                left = 0
            if right < 0:
                right = 0                
            nonlocal ans
            ans = max(ans,left+right+node.val)
            return max(left, right) + node.val
        findLargestSum(root)
        return ans