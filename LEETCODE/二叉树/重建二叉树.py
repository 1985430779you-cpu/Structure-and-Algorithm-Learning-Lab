class TreeNode():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def reConstructBinaryTree(self, preorder, inorder):
        if len(preorder) == 0: return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        else:
            root = TreeNode(preorder[0])
            pos = inorder.index(preorder[0])
            root.left = self.reConstructBinaryTree(preorder[1:pos+1], inorder[:pos])
            root.right = self.reConstructBinaryTree(preorder[pos+1:], inorder[pos+1:])
        
        return root