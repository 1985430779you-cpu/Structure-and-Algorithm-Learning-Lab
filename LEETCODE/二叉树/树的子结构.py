class TreeNode():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    #寻找是否root1子串的每个节点和root2相同
    def isSubTree(self, root1son, root2):
        if not root2:
            return  True
        if not root1son or root1son.val != root2.val:
            return  False
        return self.isSubTree(root1son.left, root2.left) and self.isSubTree(root1son.right, root2.right)
    
    #遍历root1树
    def hasSubTree(self, root1, root2):
        if not root1 or not root2:
            return  False
        return(self.isSubTree(root1, root2) or self.hasSubTree(root1.left, root2) or self.hasSubTree(root1.right, root2))
        #先判断结构，再检查左右子树

