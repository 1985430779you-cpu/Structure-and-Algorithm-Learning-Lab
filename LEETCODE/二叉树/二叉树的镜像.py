class TreeNode():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def mirrorBinaryTree(self, root):
        if root is None:
            return None

        root.left, root.right = root.right, root.left
        
        if root.left:
            self.mirrorBinaryTree(root.left)
        if root.right: 
            self.mirrorBinaryTree(root.right)
       
        return root