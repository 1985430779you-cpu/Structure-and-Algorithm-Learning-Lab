class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        
        ans = []
        def dfs(node, depth):
            if not node:
                return
            
            if depth == len(ans):
                ans.append(node.val)

            dfs(node.right, depth+1)
            dfs(node.left, depth+1)
        
        dfs(root, 0)
        return ans