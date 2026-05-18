class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        return self.isSameTree(self, root.left, root.right)

    
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        left = self.isSameTree(p.left, q.right)
        right = self.isSameTree(p.right, q.left)

        if left and right and p.val == q.val:
            return True
        else:
            return False