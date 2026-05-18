class TreeNode():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def KthNode(self, root, k):
        if not root or k <= 0:
            return None
        
        list0 = []
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            list0.append(node.val)
            inorder(node.right)

        inorder(root)
        if len(list0) < k:
            return None

        return list0[k-1]