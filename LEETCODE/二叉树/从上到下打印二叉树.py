class TreeNode():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def queueBinaryTree(self, root):
        if root is None:
            return []
        
        result = []
        queue = [root]
        #二叉树中取点也需要使用指针
        while queue:
            cur = queue.pop(0)
            result.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        
        return result

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
    print('ans=', sol.queueBinaryTree(A1))