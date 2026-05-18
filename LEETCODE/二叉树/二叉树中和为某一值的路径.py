class TreeNode():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def findPath(self, Root, integer):
        if Root is None:
            return []
        List = []
        
        def sumBinaryTree(root, result, tmp):
            tmp += root.val
            result.append(root.val)

            if tmp == integer:
                List.append(result[:]) #防止添加的都是同一个result列表

            if root.left:
                sumBinaryTree(root.left, result, tmp)
            if root.right:
                sumBinaryTree(root.right, result, tmp)
            #dfs关键代码：路径搜索到满足条件后，回退
            result.pop()
            
        sumBinaryTree(Root, [], 0)
        return List

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
    print('ans=', sol.findPath(A1,integer))