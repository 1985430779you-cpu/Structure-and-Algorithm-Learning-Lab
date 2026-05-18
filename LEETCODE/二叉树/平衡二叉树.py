class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def TreeDepth(self, root):
        if root is None:
            return 0
 
        left = self.TreeDepth(root.left)
        right = self.TreeDepth(root.right)

        if abs(right - left) > 1:
            return False
        return max(left, right) + 1 #二叉树深度递归

if __name__=='__main__':
    A1 = TreeNode(1)
    A2 = TreeNode(2)
    A3 = TreeNode(3)
    A4 = TreeNode(4)
    A5 = TreeNode(5)
    A6 = TreeNode(6)
    A7 = TreeNode(4)
 
    A1.left = A2
    A1.right = A3
    A2.left = A4
    A2.right = A5
    A3.right = A7
    A4.left = A6

    integer = 8
    sol = Solution()
    print('ans=', sol.TreeDepth(A1))