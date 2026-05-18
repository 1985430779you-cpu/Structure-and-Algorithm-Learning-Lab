class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def NextNode(self, root): #中序排序
        if not root:
            return []
        list = []
        list.extend(self.NextNode(root.left))
        list.append(root)
        list.extend(self.NextNode(root.right))
        return list

    def FindNode(self, root, node): #中序排序的下一个点
        if not root or not node:
            return None
        list = self.NextNode(root)
        for i, item in enumerate(list):
            if item == node:
                if i + 1 < len(list): #处理list最后一个数
                    return list[i+1]
                else:
                    return None
        return None

if __name__=='__main__':
    A1 = TreeNode(1)
    A2 = TreeNode(2)
    A3 = TreeNode(3)
    A4 = TreeNode(4)
    A5 = TreeNode(5)
    A6 = TreeNode(6)
    A7 = TreeNode(7)
 
    A1.left = A2
    A1.right = A3
    A2.left = A4
    A2.right = A5
    A3.right = A7
    A4.left = A6

    integer = 8
    sol = Solution()
    print('ans=', sol.FindNode(A1, A7))