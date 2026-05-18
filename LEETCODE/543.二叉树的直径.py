class Solution:
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        ans = 0
        def treedepth(node):
            if not node:
                return 0
            left = treedepth(node.left)
            right = treedepth(node.right)
            nonlocal ans
            ans = max(ans, left+right)
            return max(left,right)+1
        treedepth(root)
        return ans