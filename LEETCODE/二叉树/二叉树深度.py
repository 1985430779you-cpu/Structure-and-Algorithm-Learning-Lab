class TreeNode():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def findDepth(self, Root):
        if Root is None:
            return 0
        
        result = []
        def dfs(Root, depth):
            depth += 1
            if not Root.left and not Root.right:
                result.append(depth)
            if Root.left: dfs(Root.left, depth)
            if Root.right: dfs(Root.right, depth)

        dfs(Root, 0)
        return max(result)

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
    print('ans=', sol.findDepth(A1))