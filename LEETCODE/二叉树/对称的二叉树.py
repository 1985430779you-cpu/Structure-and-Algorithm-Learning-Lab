class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetrical(self, root):      
        if not root:
            return True
        return self.is_mirror(root.left, root.right)
        
    def is_mirror(self, left, right):
        # 两个都为空
        if not left and not right:
            return True
        # 一个为空一个不为空
        if not left or not right:
            return False
        # 值相等且子树对称
        if left.val == right.val:
            return self.is_mirror(left.left, right.right) and self.is_mirror(left.right, right.left)
        return False
    
if __name__=='__main__':
    A1 = TreeNode(1)
    A2 = TreeNode(2)
    A3 = TreeNode(2)
    A4 = TreeNode(4)
    A7 = TreeNode(4)
 
    A1.left = A2
    A1.right = A3
    A2.left = A4
    A3.right = A7

    sol = Solution()
    print('ans=', sol.isSymmetrical(A1))