class TreeNode():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        ans = []
        cur = [root]
        while cur:
            nxt = []
            value = []
            for node in cur:
                value.append(node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            ans.append(value)
            cur = nxt

        return ans