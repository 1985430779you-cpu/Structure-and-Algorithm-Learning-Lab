class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipTree(self, root):
        if not root:
            return None
    
        def mirror(node):
            if not node:
                return None
            
            left = mirror(node.left)
            right = mirror(node.right)
            node.left = right
            node.right = left

            return node
        
        mirror(root)
        return root